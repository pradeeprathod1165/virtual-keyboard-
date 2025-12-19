import cv2
from .layout import KEYS

def draw_keyboard(frame):
    h, w, _ = frame.shape
    key_w = w // 12
    key_h = h // 10

    start_x = (w - key_w * 10) // 2
    start_y = h - (key_h * 4)

    key_positions = {}

    y = start_y
    for row in KEYS:
        x = start_x + (10 - len(row)) * key_w // 2
        for key in row:
            pt1 = (x, y)
            pt2 = (x + key_w - 5, y + key_h - 5)

            cv2.rectangle(frame, pt1, pt2, (255, 0, 0), 2)
            cv2.putText(
                frame, key,
                (x + key_w // 3, y + key_h // 2),
                cv2.FONT_HERSHEY_SIMPLEX, 0.9,
                (255, 255, 255), 2
            )

            key_positions[key] = (pt1, pt2)
            x += key_w
        y += key_h

    return key_positions
