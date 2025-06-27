class Solution:
    def countIncremovableSubarrays(self, nums: list[int]) -> int:
        n = len(nums)
        count = 0

        def is_strictly_increasing(arr: list[int]) -> bool:
            if len(arr) <= 1:
                return True
            for k in range(len(arr) - 1):
                if arr[k] >= arr[k+1]:
                    return False
            return True

        for i in range(n):  # Start index of the subarray to remove (inclusive)
            for j in range(i, n):  # End index of the subarray to remove (inclusive)
                # The subarray to be removed is nums[i:j+1]
                
                # Construct the remaining array by concatenating the part before 'i'
                # and the part after 'j'
                remaining_array = nums[0:i] + nums[j+1:n]
                
                # Check if the constructed remaining array is strictly increasing
                if is_strictly_increasing(remaining_array):
                    count += 1
        
        return count