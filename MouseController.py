import pyautogui
import time
from utils import calculate_distance, smooth_move

class MouseController:
    def __init__(self, screen_w, screen_h):
        self.screen_w = screen_w
        self.screen_h = screen_h
        self.prev_x = 0
        self.prev_y = 0
        self.last_click = 0
        self.click_delay = 0.2  # 200 ms cooldown

    def move(self, raw_x, raw_y, frame_w, frame_h):
        # Convert to screen coordinates
        target_x = self.screen_w / frame_w * raw_x
        target_y = self.screen_h / frame_h * raw_y

        # Smooth using exponential moving average
        smooth_x, smooth_y = smooth_move(self.prev_x, self.prev_y, target_x, target_y)
        self.prev_x, self.prev_y = smooth_x, smooth_y
        pyautogui.moveTo(smooth_x, smooth_y)

    def click_if_close(self, point1, point2, frame_w, frame_h, threshold=40):
        # Calculate Euclidean distance in screen space
        p1 = (self.screen_w / frame_w * point1[0], self.screen_h / frame_h * point1[1])
        p2 = (self.screen_w / frame_w * point2[0], self.screen_h / frame_h * point2[1])

        dist = calculate_distance(p1, p2)
        if dist < threshold and time.time() - self.last_click > self.click_delay:
            pyautogui.click()
            self.last_click = time.time()
