def distinctDifferenceArray(nums: list[int]) -> list[int]:
    n = len(nums)
    
    prefix_distinct_counts = [0] * n
    prefix_set = set()
    for i in range(n):
        prefix_set.add(nums[i])
        prefix_distinct_counts[i] = len(prefix_set)
        
    suffix_distinct_counts = [0] * n
    suffix_set = set()
    for i in range(n - 1, -1, -1):
        suffix_distinct_counts[i] = len(suffix_set)
        suffix_set.add(nums[i])
        
    diff = [0] * n
    for i in range(n):
        diff[i] = prefix_distinct_counts[i] - suffix_distinct_counts[i]
        
    return diff