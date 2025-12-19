class TapDetector:
    def __init__(self, threshold=0.03):
        self.prev_y = None
        self.threshold = threshold
        self.is_pressed = False

    def is_tap(self, hand_landmarks):
        """
        Detects index finger tap based on vertical movement.
        Returns True only ONCE per tap.
        """

        if hand_landmarks is None:
            self.prev_y = None
            self.is_pressed = False
            return False

        # Index finger tip landmark (normalized)
        index_tip = hand_landmarks.landmark[8]
        current_y = index_tip.y

        if self.prev_y is None:
            self.prev_y = current_y
            return False

        delta_y = current_y - self.prev_y
        self.prev_y = current_y

        # Finger moving DOWN fast → press
        if delta_y > self.threshold and not self.is_pressed:
            self.is_pressed = True
            return True

        # Finger moving UP → reset
        if delta_y < -self.threshold:
            self.is_pressed = False

        return False
