```python
def latestTime(time: str) -> str:
    h1 = time[0]
    h2 = time[1]
    m1 = time[3]
    m2 = time[4]
    
    if h1 == '?' and h2 == '?':
        h1 = '2'
        h2 = '3'
    elif h1 == '?':
        if h2 <= '3':
            h1 = '2'
        else:
            h1 = '1'
    elif h2 == '?':
        if h1 == '0' or h1 == '1':
            h2 = '9'
        else:
            h2 = '3'
            
    if m1 == '?' and m2 == '?':
        m1 = '5'
        m2 = '9'
    elif m1 == '?':
        m1 = '5'
    elif m2 == '?':
        m2 = '9'
        
    return h1 + h2 + ':' + m1 + m2
```