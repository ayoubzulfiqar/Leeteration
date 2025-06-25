```python
def mostFrequent(nums, key):
    counts = {}
    for i in range(len(nums) - 1):
        if nums[i] == key:
            if nums[i + 1] in counts:
                counts[nums[i + 1]] += 1
            else:
                counts[nums[i + 1]] = 1
    
    max_count = 0
    most_frequent = -1
    
    for target, count in counts.items():
        if count > max_count:
            max_count = count
            most_frequent = target
            
    return most_frequent
```