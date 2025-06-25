```python
def is_consecutive(arr):
    """
    Check if an array of numbers is consecutive.

    Args:
        arr (list): A list of numbers.

    Returns:
        bool: True if the array is consecutive, False otherwise.
    """
    if not arr:
        return True

    n = len(arr)
    min_val = min(arr)
    max_val = max(arr)

    if max_val - min_val + 1 != n:
        return False

    seen = set()
    for num in arr:
        if num in seen:
            return False
        seen.add(num)

    return True
```