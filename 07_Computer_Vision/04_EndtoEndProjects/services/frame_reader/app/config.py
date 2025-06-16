import os
from dotenv import load_dotenv

load_dotenv()

CAMERA_URL = os.getenv("CAMERA_URL", "rtsp://your_camera_url")
VIDEO_SOURCE = os.getenv("VIDEO_SOURCE", "/data/pizza.mp4")

RABBITMQ_HOST = os.getenv("RABBITMQ_HOST", "rabbitmq")
RABBITMQ_USER = os.getenv("RABBITMQ_USER", "guest")
RABBITMQ_PASS = os.getenv("RABBITMQ_PASS", "guest")
RABBITMQ_QUEUE = os.getenv("RABBITMQ_QUEUE", "frame_queue")
RABBITMQ_EXCHANGE = os.getenv("RABBITMQ_EXCHANGE", "video_exchange")
RABBITMQ_ROUTING_KEY = os.getenv("RABBITMQ_ROUTING_KEY", "video_frame")

