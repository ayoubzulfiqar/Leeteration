def minChairs(s: str) -> int:
    current_occupancy = 0
    max_chairs_needed = 0

    for event in s:
        if event == 'E':
            current_occupancy += 1
            if current_occupancy > max_chairs_needed:
                max_chairs_needed = current_occupancy
        elif event == 'L':
            current_occupancy -= 1
    
    return max_chairs_needed