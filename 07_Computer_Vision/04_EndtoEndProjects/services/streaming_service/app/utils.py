import cv2
import os
import json
from fastapi.responses import StreamingResponse


def get_sorted_frames(folder):
    files = sorted(
        [f for f in os.listdir(folder) if f.endswith(".jpg")],
        key=lambda x: os.path.getmtime(os.path.join(folder, x))
    )
    return files

def frame_generator(folder):
    while True:
        for file in get_sorted_frames(folder):
            frame_path = os.path.join(folder, file)
            with open(frame_path, "rb") as f:
                yield (b"--frame\r\nContent-Type: image/jpeg\r\n\r\n" + f.read() + b"\r\n")


def get_latest_metadata(metadata_path):
    try:
        with open(metadata_path, "r") as f:
            return json.load(f)
    except Exception:
        return {}
