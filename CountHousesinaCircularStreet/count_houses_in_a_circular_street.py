def count_houses_in_circular_street(houses: list[int]) -> int:
    n = len(houses)
    if n == 0:
        return 0

    count = 0
    for i in range(n):
        current_house_height = houses[i]
        
        # Calculate indices for left and right neighbors using modulo for circularity
        left_neighbor_index = (i - 1 + n) % n
        right_neighbor_index = (i + 1) % n
        
        left_neighbor_height = houses[left_neighbor_index]
        right_neighbor_height = houses[right_neighbor_index]
        
        # Check if the current house is strictly taller than both its neighbors
        if current_house_height > left_neighbor_height and \
           current_house_height > right_neighbor_height:
            count += 1
            
    return count