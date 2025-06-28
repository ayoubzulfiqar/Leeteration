class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        
        # A single element is always a valid strictly increasing/decreasing subarray of length 1.
        # This also handles the case where n=1, as the loop won't run and max_len will remain 1.
        max_len = 1
        
        # current_inc_len tracks the length of the current strictly increasing subarray
        current_inc_len = 1
        
        # current_dec_len tracks the length of the current strictly decreasing subarray
        current_dec_len = 1
        
        # Iterate from the second element
        for i in range(1, n):
            # If the current element is greater than the previous one, it extends an increasing sequence.
            # It also breaks any decreasing sequence, so reset current_dec_len.
            if nums[i] > nums[i-1]:
                current_inc_len += 1
                current_dec_len = 1
            # If the current element is less than the previous one, it extends a decreasing sequence.
            # It also breaks any increasing sequence, so reset current_inc_len.
            elif nums[i] < nums[i-1]:
                current_dec_len += 1
                current_inc_len = 1
            # If the current element is equal to the previous one, both increasing and decreasing
            # sequences are broken, so reset both lengths to 1.
            else:
                current_inc_len = 1
                current_dec_len = 1
            
            # Update the maximum length found so far
            max_len = max(max_len, current_inc_len, current_dec_len)
            
        return max_len