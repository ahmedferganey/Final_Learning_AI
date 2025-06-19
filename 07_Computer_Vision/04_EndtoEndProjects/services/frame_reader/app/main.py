import threading
import logging
from video_reader import read_frames
from rabbitmq_producer import FramePublisher
from config import get_video_sources
import queue
from concurrent.futures import ThreadPoolExecutor

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

def start():
    publisher = FramePublisher()
    work_queue = queue.Queue()

    def worker():
        while True:
            src, name = work_queue.get()
            try:
                logging.info(f"[START] Reading from source: {name}")
                read_frames(src, publisher.publish_json, name)
            finally:
                work_queue.task_done()

    with ThreadPoolExecutor(max_workers=4) as executor:
        for _ in range(4):
            executor.submit(worker)

        for src, name in get_video_sources():
            work_queue.put((src, name))

        work_queue.join()

if __name__ == "__main__":
    start()

