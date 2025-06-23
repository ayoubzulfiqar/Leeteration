class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        left = 1
        right = x
        ans = 0

        while left <= right:
            mid = (left + right) // 2
            
            # Use mid * mid to avoid pow() or **
            # Check if mid*mid exceeds x to prevent potential overflow (though Python handles large ints)
            # For correctness, we compare mid*mid with x
            # If mid*mid is exactly x, we found the square root
            if mid * mid == x:
                return mid
            
            # If mid*mid is less than x, mid could be the answer, or we need to look higher
            # We store mid as a potential answer and search in the right half
            elif mid * mid < x:
                ans = mid
                left = mid + 1
            
            # If mid*mid is greater than x, mid is too large, search in the left half
            else:
                right = mid - 1
        
        return ans