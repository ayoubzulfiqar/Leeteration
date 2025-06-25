```python
def isThree(n: int) -> bool:
    if n <= 3:
        return False
    
    divisors = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            if n // i == i:
                divisors += 1
            else:
                divisors += 2
    
    return divisors == 3
```