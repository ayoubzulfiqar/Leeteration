class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # The number of odd integers up to a given number 'x' (inclusive, starting from 1)
        # can be calculated as (x + 1) // 2.
        # For example:
        # Up to 0: (0 + 1) // 2 = 0
        # Up to 1: (1 + 1) // 2 = 1 (odd: 1)
        # Up to 2: (2 + 1) // 2 = 1 (odd: 1)
        # Up to 3: (3 + 1) // 2 = 2 (odds: 1, 3)
        # Up to 7: (7 + 1) // 2 = 4 (odds: 1, 3, 5, 7)
        # Up to 10: (10 + 1) // 2 = 5 (odds: 1, 3, 5, 7, 9)

        # To find the count of odd numbers in the range [low, high] (inclusive),
        # we can subtract the count of odd numbers before 'low' from the count of odd numbers up to 'high'.
        # Count of odd numbers up to high: (high + 1) // 2
        # Count of odd numbers up to low - 1: (low - 1 + 1) // 2 simplifies to low // 2.

        # Calculate the count of odd numbers from 1 up to 'high'.
        count_up_to_high = (high + 1) // 2

        # Calculate the count of odd numbers from 1 up to 'low - 1'.
        # This effectively counts odd numbers strictly less than 'low'.
        count_up_to_low_minus_1 = low // 2

        # The difference gives the count of odd numbers within the [low, high] range.
        return count_up_to_high - count_up_to_low_minus_1