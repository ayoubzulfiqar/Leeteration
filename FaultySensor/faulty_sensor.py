```python
def solve():
    n = int(input())
    s1 = list(map(int, input().split()))
    s2 = list(map(int, input().split()))

    def check(shift):
        diffs = []
        for i in range(n - 1):
            diffs.append(s1[i+1] - s2[i])
        
        first_val = s1[0] - s2[shift]
        
        consistent = True
        for i in range(n - 1):
          if i < shift:
            if s1[i+1] - s2[i] != first_val:
              consistent = False
              break
          else:
            if s1[i+1] - s2[i] != first_val:
              consistent = False
              break
        
        if consistent:
          return True
        else:
          return False

    best_shift = -1
    for shift in range(n):
        if check(shift):
            best_shift = shift
            break

    if best_shift == -1:
      print(-1)
    else:
      print(best_shift)

solve()
```