def countElements(arr: list[int]) -> int:
    """
    Counts elements x such that x + 1 is also in arr.
    If there are duplicates in arr, count them separately.
    """
    
    # Convert the array to a set for O(1) average time lookups
    num_set = set(arr)
    
    count = 0
    # Iterate through the original array
    for num in arr:
        # Check if num + 1 exists in the set of numbers
        if (num + 1) in num_set:
            count += 1
            
    return count