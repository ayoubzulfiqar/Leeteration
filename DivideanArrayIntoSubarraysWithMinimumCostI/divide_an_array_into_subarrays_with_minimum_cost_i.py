class Solution:
    def minimumCost(self, nums: list[int]) -> int:
        n = len(nums)
        min_total_cost = float('inf')

        # The first subarray always starts at index 0. Its cost is nums[0].
        # We need to find the start indices for the second and third subarrays.
        # Let i be the start index of the second subarray.
        # Let j be the start index of the third subarray.

        # Constraints:
        # 1. The first subarray must have at least one element: nums[0...i-1] -> i >= 1
        # 2. The second subarray must have at least one element: nums[i...j-1] -> j - i >= 1 -> j > i
        # 3. The third subarray must have at least one element: nums[j...n-1] -> n - j >= 1 -> j <= n - 1

        # Combining these, i can range from 1 up to n-2 (to leave at least one element for the second and third subarrays).
        # j can range from i+1 up to n-1.

        for i in range(1, n - 1):  # i is the start index of the second subarray
            for j in range(i + 1, n):  # j is the start index of the third subarray
                current_cost = nums[0] + nums[i] + nums[j]
                min_total_cost = min(min_total_cost, current_cost)

        return min_total_cost