## config.py
# app/config.py
# config.py
import os
from dotenv import load_dotenv

class Config:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
            load_dotenv(dotenv_path="/app/.env")
            cls._instance.RABBITMQ_HOST = os.getenv("RABBITMQ_HOST", "rabbitmq")
            cls._instance.RABBITMQ_PORT = int(os.getenv("RABBITMQ_PORT", 5672))
            cls._instance.RABBITMQ_QUEUE = os.getenv("RABBITMQ_QUEUE", "frame_queue")
            cls._instance.RABBITMQ_EXCHANGE = os.getenv("RABBITMQ_EXCHANGE", "video_exchange")
            cls._instance.RABBITMQ_ROUTING_KEY = os.getenv("RABBITMQ_ROUTING_KEY", "video_frame")
            cls._instance.RABBITMQ_USER = os.getenv("RABBITMQ_USER", "guest")
            cls._instance.RABBITMQ_PASS = os.getenv("RABBITMQ_PASS", "guest")
            cls._instance.DB_HOST = os.getenv("DB_HOST", "postgres")
            cls._instance.DB_PORT = os.getenv("DB_PORT", "5432")
            cls._instance.DB_NAME = os.getenv("DB_NAME", "violations_db")
            cls._instance.DB_USER = os.getenv("DB_USER", "postgres")
            cls._instance.DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")
            cls._instance.STREAM_QUEUE = os.getenv("STREAM_QUEUE", "annotated_frames")
            cls._instance.MODEL_PATH = os.getenv("MODEL_PATH", "/app/models/yolo12m-v2.pt")
            cls._instance.STREAM_ENDPOINT = os.getenv("STREAM_ENDPOINT", "http://localhost:9000/stream")
        return cls._instance



