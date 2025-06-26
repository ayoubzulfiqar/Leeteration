class Solution:
    def sumIndicesWithKSetBits(self, nums: list[int], k: int) -> int:
        total_sum = 0
        for i in range(len(nums)):
            set_bits_count = 0
            temp_i = i
            while temp_i > 0:
                temp_i &= (temp_i - 1)
                set_bits_count += 1
            
            if set_bits_count == k:
                total_sum += nums[i]
        return total_sum