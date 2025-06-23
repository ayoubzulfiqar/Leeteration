class Solution:
    def canThreePartsEqualSum(self, arr: list[int]) -> bool:
        total_sum = sum(arr)
        
        # If the total sum is not divisible by 3, it's impossible to partition
        # into three parts with equal sums.
        if total_sum % 3 != 0:
            return False
            
        target_sum = total_sum // 3
        
        current_sum = 0
        found_parts = 0
        
        # Iterate through the array to find the first two partition points.
        # The third part will automatically have the correct sum if the total sum
        # is divisible by 3 and the first two parts sum to target_sum.
        # The crucial part is to ensure all three parts are non-empty,
        # which means the second partition must not extend to the very end of the array.
        
        for i in range(len(arr)):
            current_sum += arr[i]
            
            # If we've found the sum for the first part
            if found_parts == 0 and current_sum == target_sum:
                found_parts = 1
                current_sum = 0 # Reset current_sum to find the second part
            
            # If we've found the sum for the second part
            # This condition ensures we find the second part only after the first one.
            elif found_parts == 1 and current_sum == target_sum:
                found_parts = 2
                # At this point, we have found two parts that sum to target_sum.
                # The remaining elements in the array form the potential third part.
                # For a valid partition, this third part must be non-empty.
                # This means the current index 'i' (where the second part ends)
                # must not be the last element of the array.
                if i < len(arr) - 1:
                    return True # Found three non-empty parts