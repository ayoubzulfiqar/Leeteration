class Solution:
    def minimumRightShifts(self, nums: list[int]) -> int:
        n = len(nums)
        
        sorted_nums = sorted(nums)
        
        if nums == sorted_nums:
            return 0
        
        min_val_idx = nums.index(sorted_nums[0])
        
        num_shifts = (n - min_val_idx) % n
        
        for i in range(n):
            # The element that should be at index 'i' in the sorted array
            # is 'sorted_nums[i]'.
            # After 'num_shifts' right shifts, the element originally at
            # index '(i - num_shifts + n) % n' will move to index 'i'.
            # We check if this element from the original 'nums' matches 'sorted_nums[i]'.
            if nums[(i - num_shifts + n) % n] != sorted_nums[i]:
                return -1
                
        return num_shifts