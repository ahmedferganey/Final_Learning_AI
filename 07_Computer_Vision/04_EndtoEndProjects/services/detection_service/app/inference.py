import os
import base64
import cv2
import numpy as np
from ultralytics import YOLO

# Import required classes
from ultralytics.nn.tasks import DetectionModel
try:
    from ultralytics.nn.modules.block import C3k2
except ImportError:
    C3k2 = None  # Optional fallback

# Allowlist safe globals
import torch
if C3k2:
    torch.serialization.add_safe_globals([DetectionModel, C3k2])
else:
    torch.serialization.add_safe_globals([DetectionModel])

# Load config
MODEL_PATH = os.getenv("MODEL_PATH", "/models/yolo12m-v2.pt")

# Load model
model = YOLO(MODEL_PATH)

def run_inference(encoded_image: str) -> tuple[np.ndarray, list]:
    """Run inference on a base64-encoded image."""
    try:
        img_data = base64.b64decode(encoded_image)
        frame = cv2.imdecode(np.frombuffer(img_data, dtype=np.uint8), cv2.IMREAD_COLOR)

        if frame is None:
            raise ValueError("Failed to decode image.")

        results = model(frame)[0]

        detections = []
        for box, cls in zip(results.boxes.xyxy, results.boxes.cls):
            x1, y1, x2, y2 = map(int, box.tolist())
            label = results.names[int(cls)]
            detections.append({"label": label, "box": [x1, y1, x2, y2]})

        return frame, detections

    except Exception as e:
        print(f"[ERROR] Inference failed: {e}")
        return None, []
