class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [0] * n
        left = 0
        right = n - 1
        insert_idx = n - 1

        while left <= right:
            left_val_sq = nums[left] * nums[left]
            right_val_sq = nums[right] * nums[right]

            if left_val_sq > right_val_sq:
                result[insert_idx] = left_val_sq
                left += 1
            else:
                result[insert_idx] = right_val_sq
                right -= 1
            
            insert_idx -= 1
            
        return result