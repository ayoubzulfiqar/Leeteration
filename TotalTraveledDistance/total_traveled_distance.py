import math

def calculate_total_traveled_distance(points):
    if len(points) < 2:
        return 0.0

    total_distance = 0.0
    for i in range(len(points) - 1):
        p1 = points[i]
        p2 = points[i+1]
        distance = math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)
        total_distance += distance
    return total_distance