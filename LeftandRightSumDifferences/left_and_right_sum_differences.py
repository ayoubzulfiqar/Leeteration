class Solution:
    def leftRigthDifference(self, nums: list[int]) -> list[int]:
        n = len(nums)
        
        leftSum = [0] * n
        current_left_sum = 0
        for i in range(n):
            leftSum[i] = current_left_sum
            current_left_sum += nums[i]
            
        rightSum = [0] * n
        current_right_sum = 0
        for i in range(n - 1, -1, -1):
            rightSum[i] = current_right_sum
            current_right_sum += nums[i]
            
        answer = [0] * n
        for i in range(n):
            answer[i] = abs(leftSum[i] - rightSum[i])
            
        return answer