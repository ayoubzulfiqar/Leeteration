def maximumArea(dimensions: list[list[int]]) -> int:
    max_diagonal_squared = 0
    max_area = 0

    for length, width in dimensions:
        current_diagonal_squared = length * length + width * width
        current_area = length * width

        if current_diagonal_squared > max_diagonal_squared:
            max_diagonal_squared = current_diagonal_squared
            max_area = current_area
        elif current_diagonal_squared == max_diagonal_squared:
            max_area = max(max_area, current_area)
    
    return max_area