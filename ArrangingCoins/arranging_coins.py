class Solution:
    def arrangeCoins(self, n: int) -> int:
        low = 1
        high = n
        ans = 0
        
        while low <= high:
            mid = low + (high - low) // 2
            
            # Calculate the number of coins needed for 'mid' complete rows.
            # The sum of coins for k rows is k * (k + 1) / 2.
            # Python's integers handle arbitrary size, so overflow is not an issue.
            coins_needed = mid * (mid + 1) // 2
            
            if coins_needed <= n:
                # If 'mid' rows can be completed, it's a potential answer.
                # Try to complete more rows by increasing 'low'.
                ans = mid
                low = mid + 1
            else:
                # If 'mid' rows require too many coins, 'mid' is too high.
                # Reduce the search space by decreasing 'high'.
                high = mid - 1
                
        return ans