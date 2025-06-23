class Solution:
    def twoSumLessThanK(self, A: list[int], K: int) -> int:
        A.sort()
        
        max_sum = -1
        left = 0
        right = len(A) - 1
        
        while left < right:
            current_sum = A[left] + A[right]
            
            if current_sum < K:
                max_sum = max(max_sum, current_sum)
                left += 1
            else:
                right -= 1
                
        return max_sum