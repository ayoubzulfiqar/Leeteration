class Solution:
    def maximumTripletValue(self, nums: list[int]) -> int:
        n = len(nums)
        max_val = 0

        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    current_triplet_value = (nums[i] - nums[j]) * nums[k]
                    if current_triplet_value > max_val:
                        max_val = current_triplet_value
        
        return max_val