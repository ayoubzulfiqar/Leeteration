```python
def solve():
    n = int(input())
    a = list(map(int, input().split()))

    count = 0
    for i in range(n):
        if a[i] <= 10:
            count += 1

    print(count)

solve()
```