```python
def mostFrequentEven(nums):
    counts = {}
    for num in nums:
        if num % 2 == 0:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
    
    if not counts:
        return -1
    
    max_freq = 0
    most_frequent = -1
    
    for num, freq in counts.items():
        if freq > max_freq:
            max_freq = freq
            most_frequent = num
        elif freq == max_freq:
            most_frequent = min(most_frequent, num)
    
    return most_frequent
```