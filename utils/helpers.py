import math

def distance(p1, p2):
    """
    Calculates Euclidean distance between two points.
    Supports MediaPipe landmarks or (x, y) tuples.
    """
    x1, y1 = (p1.x, p1.y) if hasattr(p1, 'x') else p1
    x2, y2 = (p2.x, p2.y) if hasattr(p2, 'x') else p2

    return math.hypot(x1 - x2, y1 - y2)
