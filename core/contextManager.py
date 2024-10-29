import sqlite3
import logging
from contextlib import contextmanager

from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.conversational_retrieval.base import ConversationalRetrievalChain
from langchain.chains.retrieval import create_retrieval_chain
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.llms.ollama import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import FastEmbedEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
from transformers.models.paligemma.convert_paligemma_weights_to_hf import device

from data.exemples_sessions import example_sessions

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class ContextManager:
    def __init__(self, db_path, pdf_path):
        self.db_path = db_path
        self.pdf_path = pdf_path
        self.embedding_model = FastEmbedEmbeddings()
        loader = PyPDFLoader(pdf_path)

        docs = loader.load()
        self.text_splitter = RecursiveCharacterTextSplitter(chunk_size=5000000, chunk_overlap=50000)
        documents = self.text_splitter.split_documents(docs)
        self.vector_store = InMemoryVectorStore.from_documents(documents=documents, embedding=self.embedding_model)

        # Initialize database connection and ensure tables are set up
        # self._initialize_db()

    # def _initialize_db(self):
    #     with sqlite3.connect(self.db_path) as conn:
    #         cursor = conn.cursor()
    #         cursor.execute("""
    #         CREATE TABLE IF NOT EXISTS sessions (
    #             id INTEGER PRIMARY KEY,
    #             transcription TEXT,
    #             summary TEXT,
    #             timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    #         )""")
    #         conn.commit()
    #         logging.info("Database initialized successfully.")

    # @contextmanager
    # def connect_db(self):
    #     conn = sqlite3.connect(self.db_path)
    #     try:
    #         yield conn
    #     finally:
    #         conn.close()

    # def load_campaign_pdf(self):
    #     # Load and embed the campaign PDF
    #     logging.info("Loading campaign PDF and generating embeddings.")
    #     pages = self.pdf_loader.load()
    #     print(pages)
    #     documents = self.text_splitter.split_documents(pages)
    #     self.vector_store = InMemoryVectorStore.from_documents(documents=documents, embedding=self.embedding_model)

    def summarize_context(self, transcription):
        logging.info("Generating session summary based on transcription.")
        retriever = self.vector_store.as_retriever()

        # Use Llama3.2 for retrieval-augmented summarization
        llm = Ollama(model="llama3.2")
        system_prompt = (
                "Vous êtes un assistant spécialisé dans les tâches de questions-réponses. "
                "Utilisez les informations contextuelles fournies pour répondre précisément à la question posée. "
                "Assurez-vous de formuler des réponses claires, complètes et adaptées au contexte de la campagne. Tu repondra toujours en francais"
                "\n\n"
                "{context}")

        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", system_prompt),
                ("human", "{input}"),
            ]
        )

        question_answer_chain = create_stuff_documents_chain(llm, prompt)
        rag_chain = create_retrieval_chain(retriever, question_answer_chain)

        results = rag_chain.invoke({"input": "Fais moi un résumé complet de toute l'aventure, donne moi aussi les chapitre? repond en francais"})

        return results["answer"]

    # def add_session_summary(self, transcription, summary):
    #     # Save the transcription and summary in the database
    #     with self.connect_db() as conn:
    #         cursor = conn.cursor()
    #         cursor.execute(
    #             "INSERT INTO sessions (transcription, summary) VALUES (?, ?)",
    #             (transcription, summary)
    #         )
    #         conn.commit()
    #         logging.info("Session transcription and summary added to database.")

    def retrieve_campaign_context(self, transcription, top_k=5):
        # Retrieve relevant context for the given transcription
        retriever = self.vector_store.as_retriever(top_k=top_k)
        # results = retriever.retrieve(transcription)
        # context = "\n".join([doc.page_content for doc in results])
        # return context

    # def get_all_summaries(self):
    #     with self.connect_db() as conn:
    #         cursor = conn.cursor()
    #         cursor.execute("SELECT summary FROM sessions")
    #         summaries = [row[0] for row in cursor.fetchall()]
    #     return summaries

    # def get_session_summary(self, session_id):
    #     with self.connect_db() as conn:
    #         cursor = conn.cursor()
    #         cursor.execute("SELECT summary FROM sessions WHERE id=?", (session_id,))
    #         result = cursor.fetchone()
    #         return result[0] if result else None


# Main script example
if __name__ == "__main__":
    campaign_pdf_path = "../data/Odyssey_of_the_Dragonlords.pdf"  # Path to your campaign PDF
    db_path = "../data/campaign_sessions.db"  # Path to your database
    context_manager = ContextManager(db_path, campaign_pdf_path)

    # Load campaign PDF (only needs to be done once)
    # context_manager.load_campaign_pdf()

    # Example session text
    idx = 0
    # example_session_text = example_sessions[idx].session_text

    # Generate a summary for the current session
    summary = context_manager.summarize_context("")

    # Display example session summary and generated summary
    print("Session summary:", example_sessions[idx].summary)
    print("#" * 50)
    print("Generated Summary:", summary)

    # Add this session summary to the database for future reference
    # context_manager.add_session_summary(example_session_text, summary)
