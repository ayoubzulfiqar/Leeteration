class Solution:
    def solve(self, nums: list[int], k: int) -> bool:
        n = len(nums)

        def is_strictly_increasing(start_idx: int, length: int) -> bool:
            if length == 1:
                return True
            for i in range(start_idx, start_idx + length - 1):
                if nums[i] >= nums[i+1]:
                    return False
            return True

        # We are looking for two adjacent subarrays of length k.
        # The first subarray starts at index 'a' and ends at 'a + k - 1'.
        # The second subarray starts at index 'a + k' and ends at 'a + 2k - 1'.
        # The last possible starting index for the first subarray ('a')
        # is when the second subarray ends at the last element of 'nums'.
        # So, 'a + 2k - 1' must be less than 'n'.
        # 'a + 2k - 1 <= n - 1'
        # 'a <= n - 2k'
        # The loop for 'a' should therefore go from 0 up to 'n - 2k' (inclusive).
        # This means the upper bound for the range function is 'n - 2k + 1'.
        
        for a in range(n - 2 * k + 1):
            # Check if the first subarray (nums[a...a+k-1]) is strictly increasing
            if is_strictly_increasing(a, k):
                # If the first is strictly increasing, check the second adjacent subarray
                # (nums[a+k...a+2k-1])
                if is_strictly_increasing(a + k, k):
                    return True
        
        # If no such pair of adjacent strictly increasing subarrays is found after checking all possibilities
        return False