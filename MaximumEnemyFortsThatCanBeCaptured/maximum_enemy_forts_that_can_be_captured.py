def max_enemy_forts_captured(forts: list[int]) -> int:
    max_captured = 0
    current_zero_count = 0
    last_fort_type = 0

    for fort_val in forts:
        if fort_val == 0:
            if last_fort_type != 0:
                current_zero_count += 1
        else:
            if last_fort_type == 0:
                last_fort_type = fort_val
                current_zero_count = 0
            elif fort_val == last_fort_type:
                current_zero_count = 0
            else:
                max_captured = max(max_captured, current_zero_count)
                last_fort_type = fort_val
                current_zero_count = 0
    
    return max_captured