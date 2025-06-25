```python
def arraySign(nums):
    """
    Given an integer array nums, return signFunc(product)
    where product is the product of all values in the array nums.
    signFunc(x) returns:
    1 if x is positive.
    -1 if x is negative.
    0 if x is equal to 0.
    """
    product = 1
    for num in nums:
        product *= num
    if product > 0:
        return 1
    elif product < 0:
        return -1
    else:
        return 0

def signFunc(x):
    """
    Returns 1 if x is positive.
    Returns -1 if x is negative.
    Returns 0 if x is equal to 0.
    """
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0
```