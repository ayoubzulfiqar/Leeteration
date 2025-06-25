```python
def minOperations(nums):
    count = 0
    while any(nums):
        smallest_positive = float('inf')
        for num in nums:
            if num > 0 and num < smallest_positive:
                smallest_positive = num
        
        if smallest_positive == float('inf'):
            break
        
        for i in range(len(nums)):
            if nums[i] > 0:
                nums[i] -= smallest_positive
        
        count += 1
    
    return count
```