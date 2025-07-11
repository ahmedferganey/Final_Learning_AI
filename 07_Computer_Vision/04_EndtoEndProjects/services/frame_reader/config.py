# config.py
import os
from dotenv import load_dotenv

load_dotenv()  # docker-compose handles .env loading, this ensures compatibility

# 📨 RabbitMQ Config
RABBITMQ_HOST = os.getenv("RABBITMQ_HOST")
RABBITMQ_PORT = int(os.getenv("RABBITMQ_PORT", 5672))
RABBITMQ_USER = os.getenv("RABBITMQ_USER")
RABBITMQ_PASS = os.getenv("RABBITMQ_PASS")
RABBITMQ_EXCHANGE = os.getenv("RABBITMQ_EXCHANGE")
RABBITMQ_STREAMING_FRAME_QUEUE = os.getenv("RABBITMQ_STREAMING_FRAME_QUEUE")
RABBITMQ_ANNOTATED_FRAME_QUEUE = os.getenv("RABBITMQ_ANNOTATED_FRAME_QUEUE")

# 🎥 Frame Reader
VIDEO_PATH = os.getenv("VIDEO_PATH")

