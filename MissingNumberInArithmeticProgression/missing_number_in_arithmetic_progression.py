def find_missing_number_in_ap(arr):
    n = len(arr)
    
    first_term = arr[0]
    last_term = arr[-1]
    
    common_difference = (last_term - first_term) // n
    
    expected_num_terms = n + 1
    expected_sum = (expected_num_terms / 2) * (first_term + last_term)
    
    actual_sum = sum(arr)
    
    missing_number = int(expected_sum - actual_sum)
    
    return missing_number