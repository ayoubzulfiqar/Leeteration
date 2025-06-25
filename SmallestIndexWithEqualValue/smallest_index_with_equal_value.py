```python
def smallest_equal(nums):
    for i in range(len(nums)):
        if i % 10 == nums[i]:
            return i
    return -1
```