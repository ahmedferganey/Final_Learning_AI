
import os
from dotenv import load_dotenv

class Config:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            load_dotenv()
            cls._instance = super(Config, cls).__new__(cls)
            cls._instance.RABBITMQ_HOST = os.getenv("RABBITMQ_HOST", "rabbitmq")
            cls._instance.RAW_FRAME_QUEUE = os.getenv("RAW_FRAME_QUEUE", "frame_queue")
            cls._instance.ANNOTATED_FRAME_QUEUE = os.getenv("ANNOTATED_FRAME_QUEUE", "annotated_frames")
        return cls._instance

