
from src.geometry import distance
from src.geometry import average_point

print(distance((1, 2), (4, 6)))  # Expected: 5.0
print(distance((0, 0), (3, 4)))  # Expected: 5.0
print(distance((2, 2), (2, 2)))  # Expected: 0.0
print(average_point([(2, 4), (6, 8)]))