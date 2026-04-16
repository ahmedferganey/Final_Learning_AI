import os
from dotenv import load_dotenv
import logging
import socket
import re

load_dotenv()

RABBITMQ_HOST = os.getenv("RABBITMQ_HOST", "rabbitmq")
RABBITMQ_PORT = int(os.getenv("RABBITMQ_PORT", 5672))
RABBITMQ_QUEUE = os.getenv("RABBITMQ_QUEUE", "frame_queue")
RABBITMQ_EXCHANGE = os.getenv("RABBITMQ_EXCHANGE", "video_exchange")
RABBITMQ_ROUTING_KEY = os.getenv("RABBITMQ_ROUTING_KEY", "video_frame")

VIDEOS_DIR = os.getenv("VIDEOS_DIR", "/app/videos")
DEBUG = os.getenv("DEBUG", "false").lower() in ("1", "true", "yes")

if DEBUG:
    logging.getLogger().setLevel(logging.DEBUG)

VALID_EXTENSIONS = {'.mp4', '.avi', '.mov', '.mkv'}

def is_valid_rtsp(rtsp_url, timeout=2):
    """Quick TCP check to verify RTSP port (554) is reachable."""
    try:
        host = re.findall(r"rtsp://([^/:]+)", rtsp_url)[0]
        socket.create_connection((host, 554), timeout=timeout)
        logging.info(f"[CHECK] ✅ RTSP source reachable: {rtsp_url}")
        return True
    except Exception as e:
        logging.warning(f"[CHECK] ❌ RTSP unreachable: {rtsp_url} ({e})")
        return False

def is_supported_video_file(path):
    _, ext = os.path.splitext(path)
    return ext.lower() in VALID_EXTENSIONS

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
            if is_valid_rtsp(src):
                valid_sources.append((src, name))
            else:
                logging.warning(f"[CONFIG] Skipping unreachable RTSP: {src}")

        else:
            full_path = os.path.abspath(os.path.join(VIDEOS_DIR, src)) if not os.path.isabs(src) else src
            if os.path.exists(full_path) and os.access(full_path, os.R_OK):
                if is_supported_video_file(full_path):
                    logging.info(f"[CONFIG] File source: {name} at {full_path}")
                    valid_sources.append((full_path, name))
                else:
                    logging.warning(f"[CONFIG] Skipping unsupported video format: {full_path}")
            else:
                logging.warning(f"[CONFIG] Skipping missing/unreadable file: {full_path}")

    if not valid_sources:
        raise ValueError("No valid video sources found")
    return valid_sources

