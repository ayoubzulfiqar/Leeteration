class Solution:
    def findTheArrayConcatenationValue(self, nums: list[int]) -> int:
        concatenation_value = 0
        left = 0
        right = len(nums) - 1

        while left <= right:
            if left == right:
                # If only one element remains
                concatenation_value += nums[left]
            else:
                # Concatenate the first and last elements
                s1 = str(nums[left])
                s2 = str(nums[right])
                concatenated_num = int(s1 + s2)
                concatenation_value += concatenated_num
            
            # Move pointers inward
            left += 1
            right -= 1
            
        return concatenation_value