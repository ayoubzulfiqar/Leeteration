```python
def canBeIncreasing(nums):
    n = len(nums)
    
    def is_strictly_increasing(arr):
        for i in range(1, len(arr)):
            if arr[i] <= arr[i-1]:
                return False
        return True
    
    if is_strictly_increasing(nums):
        return True
    
    for i in range(n):
        temp_nums = nums[:i] + nums[i+1:]
        if is_strictly_increasing(temp_nums):
            return True
            
    return False
```