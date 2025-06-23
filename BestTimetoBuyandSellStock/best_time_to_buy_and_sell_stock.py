class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            # Calculate the potential profit if we sell on the current day
            # using the lowest buy price encountered so far.
            # If 'price' is less than 'min_price', 'price - min_price' will be negative,
            # which correctly won't update 'max_profit' if 'max_profit' is already positive.
            max_profit = max(max_profit, price - min_price)
            
            # Update 'min_price' to be the lowest price seen up to and including the current day.
            # This 'min_price' will be used for profit calculations for subsequent days.
            min_price = min(min_price, price)
            
        return max_profit