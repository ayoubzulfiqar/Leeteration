def is_non_decreasing(arr: list[int]) -> bool:
    if len(arr) <= 1:
        return True
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            return False
    return True

def minPairRemovalToSortArrayI(nums: list[int]) -> int:
    current_nums = list(nums)
    operations = 0

    while True:
        if is_non_decreasing(current_nums):
            return operations

        min_sum = float('inf')
        min_idx = -1

        for i in range(len(current_nums) - 1):
            current_sum = current_nums[i] + current_nums[i+1]
            if current_sum < min_sum:
                min_sum = current_sum
                min_idx = i

        sum_val = current_nums[min_idx] + current_nums[min_idx+1]
        current_nums = current_nums[:min_idx] + [sum_val] + current_nums[min_idx+2:]
        operations += 1