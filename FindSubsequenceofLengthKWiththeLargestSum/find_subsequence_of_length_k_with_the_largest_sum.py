```python
def maxSubsequence(nums, k):
    n = len(nums)
    indices = sorted(range(n), key=lambda i: nums[i], reverse=True)[:k]
    indices.sort()
    return [nums[i] for i in indices]
```