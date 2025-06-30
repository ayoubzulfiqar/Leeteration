import math

class Solution:
    def minPositiveSumSubarray(self, nums: list[int], l: int, r: int) -> int:
        min_positive_sum = math.inf
        n = len(nums)

        for i in range(n):
            current_sum = 0
            for j in range(i, n):
                current_sum += nums[j]
                current_length = j - i + 1

                if l <= current_length <= r:
                    if current_sum > 0:
                        min_positive_sum = min(min_positive_sum, current_sum)

        if min_positive_sum == math.inf:
            return -1
        else:
            return int(min_positive_sum)

# This is a class-based solution, typical for competitive programming platforms.
# For a direct functional solution as might be expected from the prompt, it would look like this:

def minPositiveSumSubarray_functional(nums: list[int], l: int, r: int) -> int:
    min_positive_sum = float('inf')
    n = len(nums)

    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += nums[j]
            current_length = j - i + 1

            if l <= current_length <= r:
                if current_sum > 0:
                    min_positive_sum = min(min_positive_sum, current_sum)

    if min_positive_sum == float('inf'):
        return -1
    else:
        return int(min_positive_sum)

# The problem description implies a function signature, so I will provide the class-based one.
# If the user's environment expects a standalone function, the second version is suitable.
# Given "Generate complete .py solution for:", a class-based solution is common for LeetCode-style problems.