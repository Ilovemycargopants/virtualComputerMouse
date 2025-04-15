import cv2
import pyautogui
from HandTracker import HandTracker
from MouseController import MouseController
import time

# Set up
cap = cv2.VideoCapture(1)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

screen_w, screen_h = pyautogui.size()
tracker = HandTracker()
mouse = MouseController(screen_w, screen_h)

# FPS tracking
prev_time = time.time()

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Camera not connected")
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape

    hands = tracker.find_hands(frame)

    if hands:
        tracker.draw_landmarks(frame, hands)
        for hand in hands:
            landmarks = tracker.get_landmark_positions(hand, w, h)
            index_finger = landmarks[8]
            thumb = landmarks[4]

            mouse.move(index_finger[0], index_finger[1], w, h)
            mouse.click_if_close(index_finger, thumb, w, h)

            cv2.circle(frame, index_finger, 8, (0, 255, 255), -1)
            cv2.circle(frame, thumb, 8, (255, 0, 255), -1)

    # FPS Display
    curr_time = time.time()
    fps = int(1 / (curr_time - prev_time))
    prev_time = curr_time
    cv2.putText(frame, f'FPS: {fps}', (20, 60),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Virtual Mouse", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
