import time
from threading import Thread
from audio_capture import AudioInputHandler
from whisper_model import WhisperModel
from ring_buffer import RingBuffer


class AppController:
    """Main controller for managing audio capture and Whisper transcription."""

    def __init__(self):
        self.audio_handler = AudioInputHandler()
        self.whisper_model = WhisperModel()
        self.ring_buffer = self.audio_handler.get_ring_buffer()

    def buffer_audio(self):
        """Continuously buffer data from the audio input into RingBuffer."""
        while True:
            time.sleep(0.1)  # Simulate a regular loop (adjust as necessary)

    def process_audio_every_10_sec(self):
        """Process buffered audio for transcription every 10 seconds."""
        while True:
            if len(self.ring_buffer) >= 160000:  # 10 seconds of audio
                audio_data_to_process = [self.ring_buffer.read(160000)]
                print("Sending data to Whisper for transcription...")
                self.whisper_model.transcribe(audio_data_to_process)
            else:
                time.sleep(1)

    def run(self):
        """Run the application."""
        Thread(target=self.audio_handler.stream_audio, daemon=True).start()
        Thread(target=self.process_audio_every_10_sec, daemon=True).start()

        # Keep the main thread alive
        print("Application is running...")
        while True:
            time.sleep(0.1)


if __name__ == "__main__":
    controller = AppController()
    controller.run()
