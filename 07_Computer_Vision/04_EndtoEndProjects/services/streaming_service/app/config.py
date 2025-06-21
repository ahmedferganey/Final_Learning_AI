import os
from dotenv import load_dotenv

class Config:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            load_dotenv()
            cls._instance = super(Config, cls).__new__(cls)
            cls._instance.RABBITMQ_HOST = os.getenv("RABBITMQ_HOST", "rabbitmq")
            cls._instance.RABBITMQ_QUEUE = os.getenv("STREAM_QUEUE", "annotated_frames")
        return cls._instance
