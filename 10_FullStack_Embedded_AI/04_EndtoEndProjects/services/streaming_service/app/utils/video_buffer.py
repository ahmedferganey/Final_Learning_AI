import threading

class VideoBuffer:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(VideoBuffer, cls).__new__(cls)
                    cls._instance.latest_frame = None
                    cls._instance.violation_count = 0
        return cls._instance

    def add_frame(self, frame_data: str, is_violation: bool):
        self.latest_frame = frame_data
        if is_violation:
            self.violation_count += 1

    def get_latest_frame(self):
        return self.latest_frame

    def get_violation_count(self):
        return self.violation_count
