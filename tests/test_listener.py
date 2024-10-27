import unittest

from core.audioListener import AudioListener


class TestAudioListener(unittest.TestCase):

    def setUp(self):
        """
        Setup before each test. Initializes AudioListener instance with Whisper.
        """
        self.listener = AudioListener()
        self.valid_audio_path = "data/test_audio.wav"  # Replace with an actual test file path
        self.invalid_audio_path = "data/non_existent_file.wav"
        self.no_speech_audio_path = "silence_audio.wav"  # Replace with a silence or noise-only file path

    def test_transcribe_audio_file_success(self):
        """
        Tests successful transcription from a valid audio file.
        """
        # Replace "expected transcription text" with expected content from `test_audio.wav`
        result = self.listener.transcribe_audio_file(self.valid_audio_path)
        self.assertIsNotNone(result)
        self.assertIn("bonjour ceci est pour tester le listener fin du test", result)

    def test_transcribe_audio_file_not_found(self):
        """
        Tests handling of a non-existent audio file.
        """
        result = self.listener.transcribe_audio_file(self.invalid_audio_path)
        self.assertIsNone(result)

    # def test_transcribe_audio_file_no_speech(self):
    #     """
    #     Tests handling of a file with no recognizable speech.
    #     """
    #     result = self.listener.transcribe_audio_file(self.no_speech_audio_path)
    #     self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()
