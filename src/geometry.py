
import numpy as np


def distance(p1, p2):
    """Calculate the Euclidean distance between two points."""
    return float(np.linalg.norm(np.array(p2) - np.array(p1)))

def average_point(points):
    """Calculate the average x and y coordinates of points."""
    points = np.array(points)

    return np.mean(points, axis=0)