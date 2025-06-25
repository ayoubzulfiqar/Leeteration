```python
def largest_subarray_length_k(arr, k):
    """
    Finds the largest subarray of length k in the given array.

    Args:
        arr (list): The input array.
        k (int): The length of the subarray.

    Returns:
        list: The largest subarray of length k.
    """
    if not arr or k <= 0 or k > len(arr):
        return []

    largest_subarray = arr[:k]
    for i in range(1, len(arr) - k + 1):
        if arr[i:i+k] > largest_subarray:
            largest_subarray = arr[i:i+k]

    return largest_subarray
```