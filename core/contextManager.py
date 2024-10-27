import sqlite3
import PyPDF2
import logging
import torch
from sentence_transformers import SentenceTransformer
from transformers import pipeline
import numpy as np

from sklearn.preprocessing import normalize

# Setting up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class ContextManager:
    def __init__(self, campaign_pdf_path: str, db_path: str = "session_summaries.db",
                 model_summarization: str = "facebook/bart-large-cnn",
                 model_translation: str = "google-t5/t5-base", translate: bool = False,
                 embedding_model: str = "all-MiniLM-L6-v2"):
        """
        Initializes the ContextManager with the campaign PDF and database path.

        :param campaign_pdf_path: Path to the campaign PDF file.
        :param db_path: Path to the SQLite database for storing session summaries.
        :param model_summarization: The name of the model to use for summarization.
        :param model_translation: The name of the model to use for translation.
        :param translate: Boolean indicating whether to translate the summary to French.
        :param embedding_model: Model for generating sentence embeddings.
        """
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.campaign_chunks = self.load_campaign_context(campaign_pdf_path)
        self.db_path = db_path
        self.create_database()
        self.summarizer = pipeline("summarization", model=model_summarization, device=self.device)
        self.translator = pipeline("translation_en_to_fr", model=model_translation, device=self.device)
        self.translate = translate  # Store the translate option
        self.embedding_model = SentenceTransformer(embedding_model)
        self.chunk_embeddings = self.embed_chunks(self.campaign_chunks)

        logging.info("ContextManager initialized successfully.")

    def load_campaign_context(self, pdf_path: str) -> list[str]:
        """Loads and extracts text from the campaign PDF file and chunks it."""
        logging.info(f"Loading campaign context from {pdf_path}.")
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text() + "\n"
        # Chunking the text into smaller parts for better retrieval
        return self.chunk_text(text)

    def chunk_text(self, text: str, chunk_size: int = 512) -> list[str]:
        """Chunks the campaign text into smaller parts for retrieval."""
        chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]
        logging.info(f"Text chunked into {len(chunks)} parts.")
        return chunks

    def embed_chunks(self, chunks: list[str]) -> np.ndarray:
        """Generates embeddings for the given chunks."""
        embeddings = self.embedding_model.encode(chunks)
        normalized_embeddings = normalize(embeddings)  # Normalize embeddings for better similarity comparison
        logging.info("Chunk embeddings generated successfully.")
        return normalized_embeddings

    def create_database(self):
        """Creates a SQLite database to store session summaries."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS summaries (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                session_text TEXT,
                                summary TEXT)''')
            conn.commit()
        logging.info("Database created or already exists.")

    def add_session_summary(self, session_text: str, summary: str):
        """Adds a new session summary to the database."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''INSERT INTO summaries (session_text, summary) VALUES (?, ?)''', (session_text, summary))
            conn.commit()
        logging.info("Added a new session summary to the database.")

    def get_previous_summaries(self) -> list[str]:
        """Retrieves all previous session summaries from the database."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT summary FROM summaries')
            rows = cursor.fetchall()
        logging.info(f"Retrieved {len(rows)} previous summaries from the database.")
        return [row[0] for row in rows]

    def retrieve_relevant_chunks(self, session_text: str, top_k: int = 3) -> list[str]:
        """Retrieves the most relevant chunks based on the session text."""
        session_embedding = self.embedding_model.encode([session_text])
        similarities = np.dot(self.chunk_embeddings, session_embedding.T).flatten()
        top_indices = np.argsort(similarities)[-top_k:][::-1]  # Get top_k indices
        relevant_chunks = [self.campaign_chunks[i] for i in top_indices]
        logging.info(f"Retrieved {len(relevant_chunks)} relevant chunks based on session text.")
        return relevant_chunks

    def summarize_context(self, session_text: str) -> str:
        """
        Summarizes the current session text using campaign context and previous summaries.

        :param session_text: The transcribed text of the current session.
        :return: A comprehensive summary including campaign context and previous summaries.
        """
        previous_summaries = self.get_previous_summaries()

        # Retrieve relevant chunks from the campaign context
        relevant_chunks = self.retrieve_relevant_chunks(session_text)

        # Constructing the context for the summary
        context = "\n".join(relevant_chunks) + "\n" + "\n".join(previous_summaries) + "\n" + session_text

        # Check and truncate if necessary
        max_length = 1024  # Max tokens for BART
        context_tokens = self.summarizer.tokenizer(context, return_tensors="pt").input_ids.shape[1]

        if context_tokens > max_length:
            logging.warning(f"Input exceeds max length ({max_length} tokens). Truncating input.")
            context = context[-(max_length):]  # Truncate the context to fit the model's requirements

        try:
            logging.info("Generating summary for the current session.")
            summary_en = self.summarizer(context, max_length=150, min_length=30, do_sample=False)[0]['summary_text']
            logging.info("Summary generated successfully.")

            if self.translate:
                # Translate summary to French if the option is enabled
                logging.info("Translating summary to French.")
                summary_fr = self.translator(summary_en, tgt_lang='fr')[0]['translation_text']
                logging.info("Translation to French completed successfully.")
                return summary_fr
            else:
                return summary_en  # Return English summary if translation is disabled

        except Exception as e:
            logging.error(f"Error during summarization or translation: {e}")
            return "Error generating summary."


# Example usage
if __name__ == "__main__":
    campaign_pdf_path = "../data/JO.pdf"  # Path to your campaign PDF
    context_manager = ContextManager(campaign_pdf_path)

    # Example session text
    example_session_text = "Last session, the party fought a dragon and saved the village."

    # Generate a summary for the current session
    summary = context_manager.summarize_context(example_session_text)
    print("Generated Summary:", summary)

    # Add this session summary to the database for future reference
    context_manager.add_session_summary(example_session_text, summary)
