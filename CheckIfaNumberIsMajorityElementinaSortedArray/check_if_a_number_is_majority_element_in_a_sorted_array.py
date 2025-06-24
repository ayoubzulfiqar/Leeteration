def find_first_occurrence(nums, target):
    low = 0
    high = len(nums) - 1
    first_idx = -1
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] == target:
            first_idx = mid
            high = mid - 1
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return first_idx

def isMajorityElement(nums, target):
    n = len(nums)
    if n == 0:
        return False

    first_idx = find_first_occurrence(nums, target)
    
    if first_idx == -1:
        return False
    
    if first_idx + n // 2 < n and nums[first_idx + n // 2] == target:
        return True
    
    return False