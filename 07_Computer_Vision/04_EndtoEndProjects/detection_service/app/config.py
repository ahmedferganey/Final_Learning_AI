import os

RABBITMQ_HOST = os.getenv("RABBITMQ_HOST", "localhost")
RABBITMQ_QUEUE = os.getenv("RABBITMQ_QUEUE", "frame_queue")
RABBITMQ_EXCHANGE = os.getenv("RABBITMQ_EXCHANGE", "video_exchange")
RABBITMQ_ROUTING_KEY = os.getenv("RABBITMQ_ROUTING_KEY", "video_frame")
MODEL_PATH = os.getenv("MODEL_PATH", "app/models/yolo12m-v2.pt")
ROI_ZONES = [(100, 100, 300, 300)]  # Example ROI bounding box for scooper zone

