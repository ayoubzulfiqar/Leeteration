class Solution:
    def applyOperations(self, nums: list[int]) -> list[int]:
        n = len(nums)

        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0

        write_ptr = 0
        for read_ptr in range(n):
            if nums[read_ptr] != 0:
                nums[write_ptr] = nums[read_ptr]
                write_ptr += 1
        
        while write_ptr < n:
            nums[write_ptr] = 0
            write_ptr += 1
            
        return nums