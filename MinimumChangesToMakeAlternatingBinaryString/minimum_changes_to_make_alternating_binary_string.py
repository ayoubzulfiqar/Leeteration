```python
def min_operations(s):
    n = len(s)
    
    # Option 1: Start with '0'
    count1 = 0
    for i in range(n):
        if i % 2 == 0:
            if s[i] == '1':
                count1 += 1
        else:
            if s[i] == '0':
                count1 += 1
    
    # Option 2: Start with '1'
    count2 = 0
    for i in range(n):
        if i % 2 == 0:
            if s[i] == '0':
                count2 += 1
        else:
            if s[i] == '1':
                count2 += 1
    
    return min(count1, count2)
```