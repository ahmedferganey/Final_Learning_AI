import cv2
import time
import logging
from datetime import datetime
from utils import encode_frame


def flush_camera_buffer(cap, frames_to_clear=5):
    """
    Reduce latency by clearing OpenCV's internal frame buffer.
    This is especially helpful for RTSP streams with buffering delays.
    """
    for _ in range(frames_to_clear):
        cap.grab()


def create_capture(source, source_name):
    """
    Create a VideoCapture object depending on source type (RTSP, webcam, or file).
    """
    if isinstance(source, str) and source.startswith("rtsp://"):
        logging.info(f"[{source_name}] Connecting to RTSP stream...")
        return cv2.VideoCapture(source, cv2.CAP_FFMPEG)
    else:
        logging.info(f"[{source_name}] Opening video source...")
        return cv2.VideoCapture(source)


def reconnect(cap, source, source_name, delay=2):
    """
    Attempt to reconnect to the video source with optional delay.
    """
    logging.warning(f"[{source_name}] Reconnecting to source in {delay}s...")
    cap.release()
    time.sleep(delay)
    return create_capture(source, source_name)


def read_frames(source, callback, source_name, target_fps=15, max_retries=5):
    """
    Continuously read frames from a video source and publish them using a callback.
    Handles buffering, reconnection, and frame rate control.
    """
    retry_count = 0
    cap = None

    while retry_count < max_retries:
        cap = create_capture(source, source_name)

        if not cap.isOpened():
            logging.error(f"[{source_name}] Failed to open source: {source}")
            retry_count += 1
            time.sleep(2)
            continue

        logging.info(f"[{source_name}] ✅ Stream opened successfully.")
        fps = cap.get(cv2.CAP_PROP_FPS) or 30
        frame_skip = max(1, int(fps / target_fps))
        frame_number = 0

        try:
            while True:
                flush_camera_buffer(cap, frames_to_clear=4)

                ret, frame = cap.read()
                if not ret:
                    logging.warning(f"[{source_name}] ❌ Frame read failed.")
                    cap = reconnect(cap, source, source_name)
                    break  # Break inner loop and reconnect

                frame_number += 1
                if frame_number % frame_skip != 0:
                    continue  # Drop frames to match target FPS

                h, w = frame.shape[:2]

                payload = {
                    "frame_id": frame_number,
                    "timestamp": datetime.utcnow().isoformat(),
                    "frame_data": encode_frame(frame),
                    "source": source_name,
                    "width": w,
                    "height": h
                }

                callback(payload)
                logging.info(f"[{source_name}] 📤 Published frame {frame_number}")

                time.sleep(1.0 / target_fps)

        except Exception as e:
            logging.exception(f"[{source_name}] Unexpected error: {e}")
            retry_count += 1
            time.sleep(min(5, 2 ** retry_count))

        finally:
            if cap:
                cap.release()
            logging.info(f"[{source_name}] Stream closed for reconnect.")

    logging.error(f"[{source_name}] ❌ Max retries exceeded. Giving up.")

