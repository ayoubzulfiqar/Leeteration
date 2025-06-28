import collections

class Solution:
    def get_x_sum(self, sub_array: list[int], x: int) -> int:
        """
        Calculates the x-sum of a given subarray.
        """
        counts = collections.Counter(sub_array)
        
        # Create a list of (frequency, value) tuples from the counts.
        # Example: {1:2, 2:2, 3:1, 4:1} -> [(2,1), (2,2), (1,3), (1,4)] (before sort)
        items = [(count, val) for val, count in counts.items()]
            
        # Sort the items based on the problem's criteria:
        # 1. Primary sort key: frequency (descending).
        # 2. Secondary sort key: value (descending) for tie-breaking.
        # This ensures that elements with higher frequency come first,
        # and among elements with the same frequency, the one with the larger value comes first.
        items.sort(key=lambda item: (item[0], item[1]), reverse=True)
        
        current_x_sum = 0
        # Iterate through the top 'x' most frequent elements (or fewer if there are less than 'x' distinct elements).
        # For each of these elements, add its total contribution (count * value) to the sum.
        for i in range(min(x, len(items))):
            count, val = items[i]
            current_x_sum += count * val
            
        return current_x_sum

    def xSumSubarrays(self, nums: list[int], k: int, x: int) -> list[int]:
        """
        Finds the x-sum for all k-long subarrays in the given array nums.
        """
        n = len(nums)
        answer = []
        
        # Iterate through all possible starting indices for subarrays of length k.
        # The loop runs from 0 up to n - k, inclusive.
        for i in range(n - k + 1):
            # Extract the current subarray.
            sub_array = nums[i : i + k]
            # Calculate its x-sum and append to the result list.
            answer.append(self.get_x_sum(sub_array, x))
            
        return answer

```