```python
def subsetXORSum(nums):
    def get_xor_sum(subset):
        xor_sum = 0
        for num in subset:
            xor_sum ^= num
        return xor_sum

    def get_subsets(nums):
        subsets = [[]]
        for num in nums:
            new_subsets = []
            for subset in subsets:
                new_subsets.append(subset + [num])
            subsets.extend(new_subsets)
        return subsets

    subsets = get_subsets(nums)
    total_xor_sum = 0
    for subset in subsets:
        total_xor_sum += get_xor_sum(subset)
    return total_xor_sum
```