class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        total_sum = 0
        n = len(arr)
        for i in range(n):
            # Calculate the number of possible start positions to the left of or at arr[i]
            # (indices 0 to i)
            left_count = i + 1
            
            # Calculate the number of possible end positions to the right of or at arr[i]
            # (indices i to n-1)
            right_count = n - i
            
            # Total number of subarrays that contain arr[i]
            total_subarrays_containing_i = left_count * right_count
            
            # The number of odd-length subarrays containing arr[i]
            # This is equivalent to ceil(total_subarrays_containing_i / 2)
            # If total_subarrays_containing_i is even, it's total_subarrays_containing_i / 2
            # If total_subarrays_containing_i is odd, it's (total_subarrays_containing_i + 1) / 2
            odd_length_subarrays_count = (total_subarrays_containing_i + 1) // 2
            
            # Add arr[i] multiplied by its count in odd-length subarrays to the total sum
            total_sum += arr[i] * odd_length_subarrays_count
            
        return total_sum