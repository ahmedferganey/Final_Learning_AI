import os
import cv2
import base64
from app.config import settings

def get_sorted_frame_paths():
    frames = [
        f for f in os.listdir(settings.FRAMES_PATH)
        if f.lower().endswith(".jpg")
    ]
    return sorted(frames)

def encode_frame_to_jpeg_bytes(frame):
    _, buffer = cv2.imencode(".jpg", frame)
    return buffer.tobytes()

def encode_frame_to_base64(frame):
    jpeg_bytes = encode_frame_to_jpeg_bytes(frame)
    return base64.b64encode(jpeg_bytes).decode("utf-8")

def read_frame(path):
    full_path = os.path.join(settings.FRAMES_PATH, path)
    return cv2.imread(full_path)

