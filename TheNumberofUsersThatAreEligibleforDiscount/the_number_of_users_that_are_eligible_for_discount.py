```python
def solve():
    n = int(input())
    ages = list(map(int, input().split()))
    
    count = 0
    for age in ages:
        if age >= 60 or age <= 10:
            count += 1
            
    print(count)

solve()
```