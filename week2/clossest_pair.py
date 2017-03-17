import math

def brute_force_clossest_pair(points):
    """
    2 nested for loops, quadratic time complexity
    input: points is a list of tuples
    """
    distance_min = float("inf")
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            current_distance = math.sqrt((points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2)
            if current_distance < distance_min:
                distance_min = current_distance
                point1 = points[i]
                point2 = points[j]
    return point1, point2, distance_min

assert brute_force_clossest_pair([(1, 20), (3, 4), (5, 6)]) == ((3, 4), (5, 6), 2.8284271247461903)
assert brute_force_clossest_pair([(1, 20), (13, 4),(3, 41),(3, 45),(3, 64),(53, 4),(3, 495),(30, 41),(3, 4),(3, 42),(33, 4),(3, 4.4), (5, 6)]) == ((3, 4), (3, 4.4), 0.40000000000000036)
