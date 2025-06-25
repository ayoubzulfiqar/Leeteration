```python
def getLucky(s: str, k: int) -> int:
    num_str = ""
    for char in s:
        num_str += str(ord(char) - ord('a') + 1)
    
    num = int(num_str)
    
    for _ in range(k):
        sum_digits = 0
        num_str = str(num)
        for digit in num_str:
            sum_digits += int(digit)
        num = sum_digits
    
    return num
```