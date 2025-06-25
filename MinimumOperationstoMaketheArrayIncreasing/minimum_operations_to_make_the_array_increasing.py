```python
def min_operations(nums):
    """
    Calculates the minimum number of operations to make an array strictly increasing.

    Args:
        nums: An integer array.

    Returns:
        The minimum number of operations needed to make nums strictly increasing.
    """

    operations = 0
    for i in range(1, len(nums)):
        if nums[i] <= nums[i - 1]:
            diff = nums[i - 1] - nums[i] + 1
            operations += diff
            nums[i] += diff

    return operations
```