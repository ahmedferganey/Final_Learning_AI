import os

# RabbitMQ
RABBITMQ_HOST = os.getenv("RABBITMQ_HOST", "rabbitmq")
RABBITMQ_QUEUE = os.getenv("RABBITMQ_QUEUE", "frame_queue")
RABBITMQ_USER = os.getenv("RABBITMQ_USER", "guest")
RABBITMQ_PASS = os.getenv("RABBITMQ_PASS", "guest")
RABBITMQ_EXCHANGE = os.getenv("RABBITMQ_EXCHANGE", "video_exchange")
RABBITMQ_ROUTING_KEY = os.getenv("RABBITMQ_ROUTING_KEY", "video_frame")

# Model and output
MODEL_PATH = os.getenv("MODEL_PATH", "app/models/yolo12m-v2.pt")
VIOLATION_SAVE_DIR = os.getenv("OUTPUT_PATH", "/processed_frames")

# DB and streaming service
DB_HOST = os.getenv("DB_HOST", "db")
DB_NAME = os.getenv("DB_NAME", "violations_db")
#DB_NAME = os.environ["DB_NAME"]
DB_USER = os.getenv("DB_USER", "admin")
DB_PASS = os.getenv("DB_PASS", "adminpass")

STREAMING_SERVICE_URL = os.getenv("STREAMING_SERVICE_URL", "http://streaming_service:8000/violation")

