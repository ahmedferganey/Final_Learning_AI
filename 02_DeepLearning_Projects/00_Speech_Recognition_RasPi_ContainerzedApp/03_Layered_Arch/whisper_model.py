import whisper
import numpy as np


class WhisperModel:
    """Handles Whisper model transcription."""
    def __init__(self):
        # Initialize the Whisper model
        device = "cpu"
        print(f"Using device: {device}")
        self.model = whisper.load_model("base", device=device)

    def transcribe(self, audio_chunk):
        """Transcribes audio using Whisper."""
        try:
            # Preprocess audio
            processed_audio = self.preprocess_audio(audio_chunk)
            if processed_audio is None:
                print("Failed to preprocess audio.")
                return

            # Transcribe using Whisper
            print("Transcribing audio...")
            result = self.model.transcribe(processed_audio)
            transcription = result.get("text", "")
            print("Transcription result:", transcription)

            # Save transcription to a file
            with open("/home/ahmed-ferganey/Downloads/transcription.txt", "a") as f:
                f.write(transcription + "\n")
                print("Saved transcription to file.")
        except Exception as e:
            print("Error during transcription:", e)

    def preprocess_audio(self, audio_chunk):
        """Normalize/preprocess audio data for Whisper compatibility."""
        try:
            # Clip and normalize values for Whisper expectations
            audio_chunk = np.clip(audio_chunk, -1.0, 1.0)
            return audio_chunk
        except Exception as e:
            print("Error preprocessing audio:", e)
            return None
