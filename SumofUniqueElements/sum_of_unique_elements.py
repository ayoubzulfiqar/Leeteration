```python
def sum_of_unique(nums):
    counts = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1
    
    unique_sum = 0
    for num, count in counts.items():
        if count == 1:
            unique_sum += num
    
    return unique_sum
```