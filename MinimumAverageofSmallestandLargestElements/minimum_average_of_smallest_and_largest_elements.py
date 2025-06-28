class Solution:
    def minimumAverage(self, nums: list[int]) -> float:
        nums.sort()
        
        averages = []
        left = 0
        right = len(nums) - 1
        
        while left < right:
            current_average = (nums[left] + nums[right]) / 2.0
            averages.append(current_average)
            left += 1
            right -= 1
            
        return min(averages)