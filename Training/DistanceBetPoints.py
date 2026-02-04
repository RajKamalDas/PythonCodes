import math

# Point 1
x1 = 19
y1 = 121

# Point 2
x2 = 1
y2 = 11

# Distace calculation:
dis = math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))

print(f"The distance between ({x1}, {y1}) & ({x2}, {y2}): {dis}")
