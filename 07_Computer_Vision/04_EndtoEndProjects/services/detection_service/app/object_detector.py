# app/object_detector.py

import cv2
import torch
import numpy as np
import os
from dotenv import load_dotenv

# Load YOLOv5 repo's model loader
from yolov5.models.experimental import attempt_load

# Load environment variables
load_dotenv(dotenv_path="/app/.env")
MODEL_PATH = os.getenv("MODEL_PATH", "/app/models/yolo12m-v2.pt")

# Load model globally to avoid repeated loads
model = None

def load_model(model_path=MODEL_PATH):
    global model
    if model is None:
        print(f"[DETECTION] Loading yolo12m-v2 model from {model_path}...")
        model = attempt_load(model_path, map_location=torch.device('cpu'))
        model.eval()
        print("[DETECTION] ✅ yolo12m-v2 model loaded.")
    return model

def detect_objects(frame):
    """
    Perform object detection on the input frame.
    Returns a list of dictionaries with bounding box and label info.
    """
    loaded_model = load_model()

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = loaded_model(rgb_frame, size=640)

    detections = results.xyxy[0]
    labels = loaded_model.names if hasattr(loaded_model, 'names') else results.names

    output = []
    for *box, conf, cls_id in detections:
        x1, y1, x2, y2 = map(int, box)
        label = labels[int(cls_id)]
        output.append({
            "label": label,
            "confidence": float(conf),
            "bbox": [x1, y1, x2, y2]
        })

    return output


