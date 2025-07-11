import os
import base64
import cv2
import numpy as np
from ultralytics import YOLO  # This is all you need

# Load model path from environment or default
MODEL_PATH = os.getenv("MODEL_PATH", "/app/models/yolo12m-v2.pt")

# Load YOLO model (no need for torch.load!)
model = YOLO(MODEL_PATH)

def run_inference(encoded_image):
    """Run YOLO inference on a base64-encoded image and return results."""
    try:
        # Decode the base64 image to OpenCV format
        img_data = base64.b64decode(encoded_image)
        np_arr = np.frombuffer(img_data, np.uint8)
        frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

        if frame is None:
            raise ValueError("Failed to decode image.")

        # Run YOLO model
        results = model(frame)[0]

        # Parse results
        detections = []
        for box, cls in zip(results.boxes.xyxy, results.boxes.cls):
            x1, y1, x2, y2 = map(int, box.tolist())
            label = results.names[int(cls)]
            detections.append({"label": label, "box": [x1, y1, x2, y2]})

        return frame, detections

    except Exception as e:
        print(f"❌ Inference error: {e}")
        return None, []

