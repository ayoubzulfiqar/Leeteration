```python
def solve():
    n = int(input())
    users = []
    for _ in range(n):
        users.append(list(map(int, input().split())))
    
    eligible_users = []
    for i in range(n):
        if users[i][0] > 60 and users[i][1] < 70:
            eligible_users.append(i + 1)
    
    print(*eligible_users)

solve()
```