import cv2

from camera.camera_stream import CameraStream
from hand_tracking.hand_detector import HandDetector
from keyboard.draw_keyboard import draw_keyboard
from tap_detection.tap_detector import TapDetector
from input_output.key_sender import send_key
from utils.smoother import LandmarkSmoother

smoother = LandmarkSmoother(alpha=0.8)
def main():
    cam = CameraStream(camera_index=1)  # USB phone cam
    detector = HandDetector()
    tap_detector = TapDetector()

    while True:
        ret, frame = cam.read()
        if not ret:
            print("Failed to grab frame")
            break

        # Detect hand and draw landmarks
        results = detector.detect(frame, draw=True)

        # Draw keyboard and get key positions
        key_positions = draw_keyboard(frame)

        # Process hand landmarks
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:

                # Index finger tip (normalized)
                index_tip = hand_landmarks.landmark[8]
                h, w, _ = frame.shape
                fx, fy = int(index_tip.x * w), int(index_tip.y * h)

                # Draw fingertip point
                cv2.circle(frame, (fx, fy), 10, (0, 255, 0), -1)

                # Detect tap
                if tap_detector.is_tap(hand_landmarks):
                    for key, (pt1, pt2) in key_positions.items():
                        if pt1[0] < fx < pt2[0] and pt1[1] < fy < pt2[1]:
                            send_key(key)
                            break
              

        cv2.imshow("Virtual Keyboard", frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    cam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
