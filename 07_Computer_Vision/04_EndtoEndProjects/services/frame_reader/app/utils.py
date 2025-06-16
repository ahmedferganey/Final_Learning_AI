import cv2
import base64
import logging

def encode_frame(frame):
    try:
        _, buffer = cv2.imencode('.jpg', frame)
        return base64.b64encode(buffer).decode('utf-8')
    except Exception as e:
        logging.warning(f"Encoding failed: {e}")
        return None

