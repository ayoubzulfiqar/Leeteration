```python
def findKDistantIndices(nums, key, k):
    n = len(nums)
    distant_indices = []
    for i in range(n):
        for j in range(n):
            if abs(i - j) <= k and nums[j] == key:
                distant_indices.append(i)
                break
    return sorted(list(set(distant_indices)))
```