import torch
import whisper
import sounddevice as sd
from scipy.io.wavfile import write
from threading import Thread, Event
import keyboard
from typing import Optional

class AudioListener:
    def __init__(self, backbone: str = "turbo", language: str = "fr"):
        """
        Initializes the audio listener with a Whisper model for transcription.

        :param backbone: Whisper model size to load ("tiny", "base", "small", "medium", "large").
        :param language: Language code for transcription, e.g., 'fr' for French.
        """
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model = whisper.load_model(backbone, device=self.device)
        self.language = language
        self.is_listening = False
        self.stop_event = Event()

    def listen(self, duration: int = 5) -> Optional[str]:
        """
        Listens to audio from the microphone for a specified duration and transcribes it using Whisper.

        :param duration: Duration in seconds to listen to audio.
        :return: Transcribed text or None if transcription fails.
        """
        try:
            print("Listening...")
            # Recording parameters
            sample_rate = 16000  # Whisper model expects 16kHz audio
            channels = 1  # Mono audio
            audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=channels, dtype="int16")
            sd.wait()  # Wait until the recording is finished

            # Save as WAV file temporarily
            write("temp_audio.wav", sample_rate, audio_data)

            # Transcribe the recorded audio
            result = self.model.transcribe("temp_audio.wav", language=self.language)
            text = result.get("text", "").strip()

            if text:
                print(f"Transcription (from microphone): {text}")
                return text
            else:
                print("No transcribable audio found.")
                return None

        except Exception as e:
            print(f"An error occurred during transcription: {e}")
            return None


    def transcribe_audio_file(self, file_path: str) -> Optional[str]:
        """
        Transcribes an audio file using Whisper.

        :param file_path: Path to the audio file to transcribe.
        :return: Transcribed text or None if transcription fails.
        """
        try:
            result = self.model.transcribe(file_path, language=self.language)
            text = result.get("text", "").strip()
            if text:
                return text
            else:
                print("No transcribable audio found in the file.")
                return None

        except FileNotFoundError:
            print(f"File not found: {file_path}")
            return None

        except Exception as e:
            print(f"An error occurred during transcription: {e}")
            return None

def demo_listener_file(file_path: str):
    listener = AudioListener()
    text = listener.transcribe_audio_file(file_path)
    print(f"Transcription (from file): {text}")

if __name__ == "__main__":
    listener = AudioListener()
    listener.listen(10)  # Start listening in a separate thread

    # Uncomment the line below to test file transcription
    # demo_listener_file("../data/voice_1_t.wav")
