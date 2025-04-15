import cv2
import mediapipe as mp

class HandTracker:
    def __init__(self, max_hands=1):
        self.hands = mp.solutions.hands.Hands(
            static_image_mode=False,
            max_num_hands=max_hands,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.7
        )
        self.drawing_utils = mp.solutions.drawing_utils

    def find_hands(self, frame):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(rgb)
        return results.multi_hand_landmarks

    def draw_landmarks(self, frame, hands):
        for hand in hands:
            self.drawing_utils.draw_landmarks(
                frame, hand, mp.solutions.hands.HAND_CONNECTIONS
            )

    def get_landmark_positions(self, hand, frame_width, frame_height):
        return [
            (int(lm.x * frame_width), int(lm.y * frame_height))
            for lm in hand.landmark
        ]
