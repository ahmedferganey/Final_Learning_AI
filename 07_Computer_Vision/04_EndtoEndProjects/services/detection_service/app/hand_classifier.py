# hand_classifier.py
import mediapipe as mp
import cv2


class HandActionClassifier:
    def __init__(self, debug: bool = False):
        self.hands = mp.solutions.hands.Hands(
            static_image_mode=False,
            max_num_hands=2,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )
        self.motion_state = {}  # {track_id: "grabbing"/"cleaning"}
        self.debug = debug

    def update(self, hand_id, frame, bbox):
        """
        Update the internal state of the given hand track.
        Args:
            hand_id: Track ID of the hand.
            frame: Full image frame (BGR).
            bbox: [x1, y1, x2, y2] bounding box of the hand.
        """
        try:
            x1, y1, x2, y2 = bbox
            cropped = frame[y1:y2, x1:x2]
            if cropped.size == 0:
                if self.debug:
                    print(f"[HAND] Empty crop for hand ID {hand_id}, skipping.")
                return

            rgb = cv2.cvtColor(cropped, cv2.COLOR_BGR2RGB)
            result = self.hands.process(rgb)

            if result.multi_hand_landmarks:
                landmarks = result.multi_hand_landmarks[0].landmark
                thumb_tip = landmarks[4]
                index_tip = landmarks[8]

                dist = ((thumb_tip.x - index_tip.x) ** 2 + (thumb_tip.y - index_tip.y) ** 2) ** 0.5

                # You can tune this threshold based on observed behavior
                if dist < 0.1:
                    state = "grabbing"
                else:
                    state = "cleaning"

                self.motion_state[hand_id] = state
                if self.debug:
                    print(f"[HAND] ID {hand_id} → {state} (dist={dist:.3f})")
            else:
                self.motion_state[hand_id] = "cleaning"
                if self.debug:
                    print(f"[HAND] ID {hand_id} → cleaning (no landmarks)")

        except Exception as e:
            print(f"[HAND] ⚠️ Failed to classify hand ID {hand_id}: {e}")
            self.motion_state[hand_id] = "cleaning"

    def classify(self, hand_id):
        """
        Get the last known action for a hand.
        """
        return self.motion_state.get(hand_id, "cleaning")

