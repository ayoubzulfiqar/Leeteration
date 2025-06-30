class Solution:
    def sumOfGoodNumbers(self, nums: list[int], k: int) -> int:
        total_sum = 0
        n = len(nums)

        for i in range(n):
            is_current_good = True

            # Check condition for index i - k
            left_idx = i - k
            if left_idx >= 0:  # If the left index exists
                if nums[i] <= nums[left_idx]:
                    is_current_good = False
            
            # Check condition for index i + k
            right_idx = i + k
            if right_idx < n:  # If the right index exists
                if nums[i] <= nums[right_idx]:
                    is_current_good = False
            
            # If after checking all applicable conditions, the number is still good
            if is_current_good:
                total_sum += nums[i]
        
        return total_sum