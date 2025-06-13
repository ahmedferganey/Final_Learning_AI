import cv2

def encode_frame(frame):
    success, buffer = cv2.imencode('.jpg', frame)
    return buffer.tobytes() if success else None

