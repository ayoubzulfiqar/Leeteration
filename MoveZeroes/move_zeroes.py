class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero_ptr = 0

        for read_ptr in range(len(nums)):
            if nums[read_ptr] != 0:
                nums[non_zero_ptr] = nums[read_ptr]
                non_zero_ptr += 1
        
        for i in range(non_zero_ptr, len(nums)):
            nums[i] = 0