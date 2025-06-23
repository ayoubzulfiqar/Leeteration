class Solution:
    def findShortestSubArray(self, nums: list[int]) -> int:
        first_occurrence = {}
        last_occurrence = {}
        counts = {}

        for i, num in enumerate(nums):
            if num not in first_occurrence:
                first_occurrence[num] = i
            last_occurrence[num] = i
            counts[num] = counts.get(num, 0) + 1

        degree = 0
        if counts: # Handle case where nums is empty, though constraints say non-empty
            degree = max(counts.values())
        else:
            return 0 # Should not happen based on constraints (non-empty array)

        min_length = float('inf')

        for num, count in counts.items():
            if count == degree:
                length = last_occurrence[num] - first_occurrence[num] + 1
                min_length = min(min_length, length)

        return min_length