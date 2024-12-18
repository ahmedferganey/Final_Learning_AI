import tkinter as tk
from audio_capture import AudioInputHandler
from whisper_model import WhisperTranscriber


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Audio Stream Transcription")
        self.geometry("400x200")

        self.audio_handler = AudioInputHandler(max_duration=60)
        self.transcriber = WhisperTranscriber()

        # Button to control streaming
        self.start_button = tk.Button(self, text="Start Streaming", command=self.start_streaming)
        self.start_button.pack(pady=10)

        self.stop_button = tk.Button(self, text="Stop Streaming", command=self.stop_streaming)
        self.stop_button.pack(pady=10)

        self.transcribe_button = tk.Button(self, text="Transcribe", command=self.transcribe_audio)
        self.transcribe_button.pack(pady=10)

        self.streaming = False

    def start_streaming(self):
        if not self.streaming:
            print("Starting streaming...")
            self.audio_handler.start_stream()
            self.streaming = True

    def stop_streaming(self):
        if self.streaming:
            print("Stopping streaming...")
            self.audio_handler.stop_stream()
            self.streaming = False
            print("Stopped streaming.")

    def transcribe_audio(self):
        print("Transcribing last 1 minute of audio...")
        audio_data = self.audio_handler.get_last_minute_data()
        transcription_result = self.transcriber.transcribe(audio_data)
        print("Transcription result:", transcription_result)


if __name__ == "__main__":
    app = Application()
    app.mainloop()
