class Solution:
    def minSubsequence(self, nums: list[int]) -> list[int]:
        nums.sort(reverse=True)
        total_sum = sum(nums)
        
        current_subsequence_sum = 0
        subsequence = []
        
        for num in nums:
            subsequence.append(num)
            current_subsequence_sum += num
            
            if current_subsequence_sum * 2 > total_sum:
                break
                
        return subsequence