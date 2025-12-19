import cv2

class CameraStream:
    def __init__(self, camera_index=1, width=960, height=720):
        self.cap = cv2.VideoCapture(camera_index)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

    def read(self):
        ret, frame = self.cap.read()
        if not ret:
            return ret, frame

        # MIRROR IMAGE FOR NATURAL MOVEMENT
        frame = cv2.flip(frame, 1)
        return ret, frame

    def release(self):
        self.cap.release()
