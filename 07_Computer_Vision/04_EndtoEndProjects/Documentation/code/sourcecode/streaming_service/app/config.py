
import os

class Settings:
    FRAMES_PATH = os.getenv("FRAMES_PATH", "/processed_frames")
    STREAM_PORT = int(os.getenv("STREAM_PORT", 8004))
    STREAM_FPS = float(os.getenv("STREAM_FPS", 25))
    METADATA_PATH = os.getenv("METADATA_PATH", "shared/processed_frames/metadata.json")

settings = Settings()
