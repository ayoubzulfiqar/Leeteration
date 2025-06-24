class Solution:
    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        consecutive_odds_count = 0
        for num in arr:
            if num % 2 != 0:  # Check if the number is odd
                consecutive_odds_count += 1
                if consecutive_odds_count == 3:
                    return True
            else:
                consecutive_odds_count = 0
        return False