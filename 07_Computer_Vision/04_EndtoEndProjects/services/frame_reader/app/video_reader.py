import cv2
import time
import logging
from datetime import datetime
from utils import encode_frame

def read_frames(source, callback, source_name, target_fps=15, max_retries=3):
    retry_count = 0
    cap = None

    while retry_count < max_retries:
        try:
            if isinstance(source, str) and source.startswith("rtsp://"):
                cap = cv2.VideoCapture(source, cv2.CAP_FFMPEG)
            else:
                cap = cv2.VideoCapture(source)

            if not cap.isOpened():
                raise IOError(f"Failed to open source: {source}")

            fps = cap.get(cv2.CAP_PROP_FPS)
            if fps <= 1e-2:
                fps = 30

            frame_skip = max(1, int(fps / target_fps))
            frame_number = 0

            logging.info(f"[{source_name}] ✅ Started streaming at {target_fps} FPS")

            while True:
                ret, frame = cap.read()
                if not ret:
                    logging.warning(f"[{source_name}] Frame read failed. Reconnecting...")
                    break

                frame_number += 1
                if frame_number % frame_skip != 0:
                    continue

                h, w = frame.shape[:2]
                frame_data = encode_frame(frame)
                if not frame_data:
                    logging.warning(f"[{source_name}] Skipped frame {frame_number} due to encoding failure.")
                    continue

                payload = {
                    "frame_id": frame_number,
                    "timestamp": datetime.now().isoformat(),
                    "frame_data": frame_data,
                    "source": source_name,
                    "width": w,
                    "height": h
                }

                callback(payload)
                time.sleep(1.0 / target_fps)

        except Exception as e:
            logging.error(f"[{source_name}] Error: {e}")
            retry_count += 1
            time.sleep(5)

        finally:
            if cap:
                cap.release()

    logging.error(f"[{source_name}] Max retries ({max_retries}) exceeded.")

