import mediapipe as mp
import cv2

class HandActionClassifier:
    def __init__(self):
        self.hands = mp.solutions.hands.Hands(static_image_mode=False, max_num_hands=2)
        self.motion_state = {}  # id -> last movement state (grabbing or cleaning)

    def update(self, hand_id, frame, bbox):
        x1, y1, x2, y2 = bbox
        cropped = frame[y1:y2, x1:x2]
        if cropped.size == 0:
            return
        rgb = cv2.cvtColor(cropped, cv2.COLOR_BGR2RGB)
        result = self.hands.process(rgb)

        if result.multi_hand_landmarks:
            # Use thumb tip and index tip to guess action
            landmarks = result.multi_hand_landmarks[0].landmark
            thumb_tip = landmarks[4]
            index_tip = landmarks[8]
            dist = ((thumb_tip.x - index_tip.x) ** 2 + (thumb_tip.y - index_tip.y) ** 2) ** 0.5
            self.motion_state[hand_id] = "grabbing" if dist < 0.1 else "cleaning"
        else:
            self.motion_state[hand_id] = "cleaning"

    def classify(self, hand_id):
        return self.motion_state.get(hand_id, "cleaning")

