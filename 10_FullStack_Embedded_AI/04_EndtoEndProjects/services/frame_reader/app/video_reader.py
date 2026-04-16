import cv2
import time
import logging
from datetime import datetime
from utils import encode_frame
from concurrent.futures import ThreadPoolExecutor, TimeoutError

# Create a single-thread executor for timed reads
read_executor = ThreadPoolExecutor(max_workers=1)

def flush_camera_buffer(cap, max_frames=10):
    for _ in range(max_frames):
        cap.grab()

def create_capture(source, source_name):
    logging.info(f"[{source_name}] Opening stream...")
    cap = cv2.VideoCapture(
        source,
        cv2.CAP_FFMPEG if isinstance(source, str) and source.startswith("rtsp://") else cv2.CAP_ANY
    )
    cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
    return cap

def is_frame_stale(prev_frame, curr_frame):
    return prev_frame is not None and cv2.norm(prev_frame, curr_frame) < 1e-6

def read_frame_with_timeout(cap, timeout=2.0):
    """Attempt to read a frame with timeout protection."""
    future = read_executor.submit(cap.read)
    try:
        return future.result(timeout=timeout)
    except TimeoutError:
        logging.error("[Reader] ❌ cap.read() timed out.")
        return False, None

def read_frames(source, callback, source_name, target_fps=15, max_retries=5, shutdown_event=None):
    if shutdown_event is None:
        raise ValueError("Missing shutdown_event")

    retry_count = 0
    prev_frame = None

    while retry_count < max_retries and not shutdown_event.is_set():
        cap = create_capture(source, source_name)

        if not cap.isOpened():
            logging.error(f"[{source_name}] Failed to open source: {source}")
            retry_count += 1
            time.sleep(2)
            continue

        logging.info(f"[{source_name}] ✅ Stream opened successfully.")
        frame_number = 0
        frame_interval = 1.0 / target_fps

        try:
            while not shutdown_event.is_set():
                flush_camera_buffer(cap)
                start_time = time.time()

                ret, frame = read_frame_with_timeout(cap, timeout=2.0)
                if not ret or is_frame_stale(prev_frame, frame):
                    logging.warning(f"[{source_name}] ❌ Bad/stale/timed-out frame. Reconnecting...")
                    break

                frame_number += 1
                prev_frame = frame

                h, w = frame.shape[:2]
                encoded = encode_frame(frame, resize=(640, 480))
                if not encoded:
                    logging.warning(f"[{source_name}] ⚠️ Skipped frame {frame_number} due to encoding failure.")
                    continue

                payload = {
                    "frame_id": frame_number,
                    "timestamp": datetime.utcnow().isoformat(),
                    "frame_data": encoded,
                    "source": source_name,
                    "width": w,
                    "height": h
                }

                if callback(payload):
                  logging.info(f"[{source_name}] 📤 Published frame {frame_number}")
                else:
                  logging.warning(f"[{source_name}] ❌ Failed to publish frame {frame_number} after retries.")

                elapsed = time.time() - start_time
                time.sleep(max(0, frame_interval - elapsed))

        except Exception as e:
            logging.exception(f"[{source_name}] Unexpected error: {e}")
            retry_count += 1
            time.sleep(min(5, 2 ** retry_count))

        finally:
            cap.release()
            logging.info(f"[{source_name}] Stream closed.")

    if retry_count >= max_retries:
        logging.error(f"[{source_name}] ❌ Max retries exceeded. Giving up.")

