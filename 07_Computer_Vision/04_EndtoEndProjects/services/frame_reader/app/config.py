import os
from dotenv import load_dotenv
import logging

load_dotenv()

RABBITMQ_HOST = os.getenv("RABBITMQ_HOST", "rabbitmq")
RABBITMQ_PORT = int(os.getenv("RABBITMQ_PORT", 5672))
RABBITMQ_QUEUE = os.getenv("RABBITMQ_QUEUE", "frame_queue")
RABBITMQ_EXCHANGE = os.getenv("RABBITMQ_EXCHANGE", "video_exchange")
RABBITMQ_ROUTING_KEY = os.getenv("RABBITMQ_ROUTING_KEY", "video_frame")

def get_video_sources():
    paths = [p.strip() for p in os.getenv("VIDEO_SOURCES", "").split(",") if p.strip()]
    names = [n.strip() for n in os.getenv("SOURCE_NAMES", "").split(",") if n.strip()]

    logging.info(f"[CONFIG] VIDEO_SOURCES: {paths}")
    logging.info(f"[CONFIG] SOURCE_NAMES: {names}")

    if not paths or not names:
        raise ValueError("VIDEO_SOURCES or SOURCE_NAMES is empty")
    if len(paths) != len(names):
        raise ValueError("VIDEO_SOURCES and SOURCE_NAMES length mismatch")

    valid_sources = []
    for src, name in zip(paths, names):
        if src.isdigit():
            logging.info(f"[CONFIG] Webcam source: {name} (device {src})")
            valid_sources.append((int(src), name))
        elif src.startswith("rtsp://"):
            logging.info(f"[CONFIG] RTSP source: {name} ({src})")
            valid_sources.append((src, name))
        else:
            full_path = os.path.abspath(src)
            if os.path.exists(full_path):
                logging.info(f"[CONFIG] File source: {name} at {full_path}")
                valid_sources.append((full_path, name))
            else:
                logging.warning(f"[CONFIG] Skipping missing file: {full_path}")

    if not valid_sources:
        raise ValueError("No valid video sources found")
    return valid_sources

