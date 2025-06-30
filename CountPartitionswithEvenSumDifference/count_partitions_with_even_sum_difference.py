class Solution:
    def countEvenSumDifferencePartitions(self, nums: list[int]) -> int:
        n = len(nums)
        total_sum = sum(nums)

        # The difference between the sum of the left subarray (S_L)
        # and the sum of the right subarray (S_R) is S_L - S_R.
        # We know that S_R = total_sum - S_L.
        # So, S_L - S_R = S_L - (total_sum - S_L) = 2 * S_L - total_sum.

        # For (2 * S_L - total_sum) to be even:
        # Since 2 * S_L is always an even number,
        # the parity of (2 * S_L - total_sum) depends entirely on the parity of total_sum.
        # If total_sum is odd: (even - odd) = odd. The difference will always be odd.
        # If total_sum is even: (even - even) = even. The difference will always be even.

        # Therefore, the difference (S_L - S_R) is even if and only if the total_sum of the array is even.

        if total_sum % 2 != 0:
            # If the total sum is odd, no partition will result in an even sum difference.
            return 0
        else:
            # If the total sum is even, every valid partition will result in an even sum difference.
            # A valid partition index 'i' ranges from 0 to n-2 (inclusive).
            # This means there are (n-2) - 0 + 1 = n-1 possible partitions.
            return n - 1