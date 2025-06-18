# frame_reader/app/config.py
import os
from dotenv import load_dotenv
from shared import constants

load_dotenv()

# ============================
# 🎥 Camera Configuration
# ============================
CAMERA_URL = os.getenv("CAMERA_URL", constants.DEFAULT_VIDEO_PATH)

if CAMERA_URL.startswith("rtsp://"):
    SOURCE_TYPE = "RTSP"
elif os.path.exists(CAMERA_URL):
    SOURCE_TYPE = "LOCAL_FILE"
else:
    SOURCE_TYPE = "UNKNOWN"

print(f"[CONFIG] Using {SOURCE_TYPE} source: {CAMERA_URL}")

# ============================
# 📨 RabbitMQ Configuration
# ============================
RABBITMQ_HOST = os.getenv("RABBITMQ_HOST", "rabbitmq")
RABBITMQ_USER = os.getenv("RABBITMQ_USER", "guest")
RABBITMQ_PASS = os.getenv("RABBITMQ_PASS", "guest")
RABBITMQ_QUEUE = os.getenv("RABBITMQ_QUEUE", "frame_queue")
RABBITMQ_EXCHANGE = os.getenv("RABBITMQ_EXCHANGE", "video_exchange")
RABBITMQ_ROUTING_KEY = os.getenv("RABBITMQ_ROUTING_KEY", "video_frame")

