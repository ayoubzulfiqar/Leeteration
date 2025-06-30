class Solution:
    def countSubarrays(self, nums: list[int]) -> int:
        count = 0
        # Iterate through the array to find all possible starting positions
        # for a subarray of length 3.
        # A subarray of length 3 starting at index `i` will include elements
        # at indices `i`, `i+1`, and `i+2`.
        # Therefore, the last possible starting index `i` is `len(nums) - 3`.
        # The range function `range(N)` goes from 0 up to N-1.
        # So, `range(len(nums) - 2)` covers indices from 0 up to `len(nums) - 3`.
        for i in range(len(nums) - 2):
            # Get the three numbers of the current subarray
            first_num = nums[i]
            second_num = nums[i+1]
            third_num = nums[i+2]

            # Check the condition: sum of the first and third numbers equals
            # exactly half of the second number.
            # To avoid potential floating-point precision issues and to handle
            # cases where the second number might be odd (where its half would
            # not be an integer), it's safer to multiply both sides by 2.
            # The condition (first_num + third_num) == (second_num / 2)
            # is mathematically equivalent to 2 * (first_num + third_num) == second_num.
            if 2 * (first_num + third_num) == second_num:
                count += 1
        return count