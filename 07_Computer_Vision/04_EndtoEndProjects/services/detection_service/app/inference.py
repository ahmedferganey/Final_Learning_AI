from ultralytics import YOLO
import cv2
import numpy as np
import io
import base64
from app.config import MODEL_PATH

model = YOLO(MODEL_PATH)

def run_inference(encoded_image):
    img_data = base64.b64decode(encoded_image)
    np_arr = np.frombuffer(img_data, np.uint8)
    frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

    results = model(frame)[0]

    detections = []
    for box, cls in zip(results.boxes.xyxy, results.boxes.cls):
        x1, y1, x2, y2 = map(int, box.tolist())
        label = results.names[int(cls)]
        detections.append({"label": label, "box": [x1, y1, x2, y2]})

    return frame, detections

