def find_max_circular_diff(nums):
    n = len(nums)
    if n < 2:
        return 0 

    max_diff = 0

    for i in range(n - 1):
        max_diff = max(max_diff, abs(nums[i] - nums[i+1]))

    max_diff = max(max_diff, abs(nums[n-1] - nums[0]))

    return max_diff