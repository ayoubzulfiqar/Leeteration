```python
def findSubarrays(nums):
    sums = set()
    for i in range(len(nums) - 1):
        current_sum = nums[i] + nums[i + 1]
        if current_sum in sums:
            return True
        sums.add(current_sum)
    return False
```