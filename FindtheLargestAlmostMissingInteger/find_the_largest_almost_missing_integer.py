import collections

class Solution:
    def findLargestAlmostMissing(self, nums: list[int], k: int) -> int:
        n = len(nums)
        
        # Dictionary to store the count of subarrays each number appears in
        # The key is the number, the value is the count of k-sized subarrays it appears in
        num_subarray_counts = collections.defaultdict(int)

        # Iterate through all possible starting indices for a subarray of size k
        # The loop runs from 0 up to n - k (inclusive)
        for i in range(n - k + 1):
            # Extract the current subarray of size k
            current_subarray = nums[i : i + k]
            
            # To correctly count how many *subarrays* a number appears in,
            # we need to consider each unique number within the current subarray only once.
            # Using a set ensures we process each distinct number in the subarray just once.
            unique_elements_in_subarray = set(current_subarray)
            
            # For each unique number found in the current subarray, increment its global count
            for num in unique_elements_in_subarray:
                num_subarray_counts[num] += 1
        
        # List to store numbers that are "almost missing" (appear in exactly one subarray)
        almost_missing_candidates = []
        
        # Iterate through the collected counts
        for num, count in num_subarray_counts.items():
            # If a number appears in exactly one subarray of size k, it's a candidate
            if count == 1:
                almost_missing_candidates.append(num)
        
        # If no such integer exists, return -1
        if not almost_missing_candidates:
            return -1
        else:
            # Otherwise, return the largest among the almost missing integers
            return max(almost_missing_candidates)