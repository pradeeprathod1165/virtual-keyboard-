from pynput.keyboard import Controller
import time

keyboard = Controller()

_last_press_time = 0
PRESS_DELAY = 0.3  # seconds

def send_key(key):
    global _last_press_time

    current_time = time.time()

    # Prevent rapid repeated presses
    if current_time - _last_press_time < PRESS_DELAY:
        return

    try:
        keyboard.press(key)
        keyboard.release(key)
        _last_press_time = current_time
        print(f"Key pressed: {key}")
    except Exception as e:
        print(f"Failed to send key {key}: {e}")
