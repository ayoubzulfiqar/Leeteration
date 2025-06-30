class Solution:
    def transformedArray(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [0] * n

        for i in range(n):
            current_val = nums[i]

            if current_val == 0:
                result[i] = 0
            else:
                # Calculate the landing index using modulo for circular behavior.
                # Python's % operator correctly handles negative results of (i + current_val)
                # to wrap around to positive indices from the end of the array.
                landing_index = (i + current_val) % n
                
                # Set result[i] to the value found at the landing index in the original nums array.
                result[i] = nums[landing_index]
        
        return result