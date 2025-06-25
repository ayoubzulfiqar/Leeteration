```python
def sort_even_odd(nums):
    odd_indices = []
    even_indices = []
    for i in range(len(nums)):
        if i % 2 == 0:
            even_indices.append(nums[i])
        else:
            odd_indices.append(nums[i])
    
    even_indices.sort()
    odd_indices.sort(reverse=True)
    
    result = []
    even_idx = 0
    odd_idx = 0
    for i in range(len(nums)):
        if i % 2 == 0:
            result.append(even_indices[even_idx])
            even_idx += 1
        else:
            result.append(odd_indices[odd_idx])
            odd_idx += 1
    
    return result
```