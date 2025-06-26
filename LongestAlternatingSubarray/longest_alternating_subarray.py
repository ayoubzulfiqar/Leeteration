class Solution:
    def longestAlternatingSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        max_len = -1
        current_len = 0
        expected_diff = 0

        for i in range(n - 1):
            diff = nums[i+1] - nums[i]

            if current_len == 0:
                if diff == 1:
                    current_len = 2
                    max_len = max(max_len, current_len)
                    expected_diff = -1
            else:
                if diff == expected_diff:
                    current_len += 1
                    max_len = max(max_len, current_len)
                    expected_diff = -expected_diff
                else:
                    if diff == 1:
                        current_len = 2
                        max_len = max(max_len, current_len)
                        expected_diff = -1
                    else:
                        current_len = 0
                        expected_diff = 0
        
        return max_len