```python
def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    ad_free_days = 0
    consecutive_days = 0
    
    for i in range(n):
        if a[i] == 0:
            consecutive_days += 1
            if consecutive_days >= k:
                ad_free_days += 1
                consecutive_days = 0
        else:
            consecutive_days = 0
            
    print(ad_free_days)

solve()
```