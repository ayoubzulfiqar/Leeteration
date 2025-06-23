def shortest_distance_in_line(points):
    if len(points) < 2:
        return float('inf')

    sorted_points = sorted(points)
    
    min_dist = float('inf')
    
    for i in range(len(sorted_points) - 1):
        current_dist = sorted_points[i+1] - sorted_points[i]
        if current_dist == 0:
            return 0
        if current_dist < min_dist:
            min_dist = current_dist
            
    return min_dist

if __name__ == "__main__":
    print(shortest_distance_in_line([1, 5, 2, 8]))
    print(shortest_distance_in_line([10, 20, 30]))
    print(shortest_distance_in_line([5]))
    print(shortest_distance_in_line([]))
    print(shortest_distance_in_line([3.14, 2.71, 1.618]))
    print(shortest_distance_in_line([7, 7, 7]))
    print(shortest_distance_in_line([-5, -1, -10, 2]))