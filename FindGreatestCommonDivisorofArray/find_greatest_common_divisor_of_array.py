```python
def find_gcd(a, b):
    while(b):
        a, b = b, a % b
    return a

def find_gcd_of_array(nums):
    smallest = min(nums)
    largest = max(nums)
    return find_gcd(smallest, largest)
```