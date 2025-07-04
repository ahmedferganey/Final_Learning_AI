# main.py

import threading
import logging
import queue
import signal
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from video_reader import read_frames
from rabbitmq_producer import FramePublisher
from config import get_video_sources

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

shutdown_event = threading.Event()
work_queue = queue.Queue()

def signal_handler(sig, frame):
    logging.info("🔴 Caught termination signal. Shutting down gracefully...")
    shutdown_event.set()

signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

def worker():
    while not shutdown_event.is_set():
        try:
            src, name = work_queue.get(timeout=1)
        except queue.Empty:
            continue

        try:
            logging.info(f"[START] 🎥 Reading from source: {name}")
            read_frames(src, publisher.publish_json, name, shutdown_event=shutdown_event)
        except Exception as e:
            logging.exception(f"[ERROR] Failed to process source {name}: {e}")
        finally:
            work_queue.task_done()

def start():
    global publisher
    publisher = FramePublisher()

    video_sources = get_video_sources()
    max_workers = max(4, len(video_sources))  # 🧠 scale to number of sources

    logging.info(f"[INIT] 🧵 Launching {max_workers} threads for {len(video_sources)} sources.")

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        for _ in range(max_workers):
            executor.submit(worker)

        for src, name in video_sources:
            work_queue.put((src, name))

        try:
            while not shutdown_event.is_set():
                time.sleep(1)
        except KeyboardInterrupt:
            signal_handler(None, None)

        logging.info("🛑 Waiting for threads to finish...")
        work_queue.join()
        logging.info("✅ All tasks completed. Exiting.")

if __name__ == "__main__":
    start()

