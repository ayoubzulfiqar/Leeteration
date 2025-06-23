class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        # Initialize for base cases:
        # dp[1] = 1 (1 way: 1)
        # dp[2] = 2 (2 ways: 1+1, 2)
        # We use two variables to store the last two results
        # a will store dp[i-2]
        # b will store dp[i-1]
        a = 1 
        b = 2 
        
        # Iterate from n = 3 up to the given n
        for _ in range(3, n + 1):
            # dp[i] = dp[i-1] + dp[i-2]
            current_ways = a + b
            # Update a and b for the next iteration
            a = b
            b = current_ways
            
        return b