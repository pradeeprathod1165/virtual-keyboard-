class LandmarkSmoother:
    def __init__(self, alpha=0.7):
        self.alpha = alpha
        self.prev_x = None
        self.prev_y = None

    def smooth(self, x, y):
        if self.prev_x is None:
            self.prev_x, self.prev_y = x, y
            return x, y

        x = int(self.alpha * self.prev_x + (1 - self.alpha) * x)
        y = int(self.alpha * self.prev_y + (1 - self.alpha) * y)

        self.prev_x, self.prev_y = x, y
        return x, y
