class Solution:
    def buyChocolates(self, prices: list[int], money: int) -> int:
        prices.sort()
        
        cost_of_two_cheapest = prices[0] + prices[1]
        
        if money >= cost_of_two_cheapest:
            return money - cost_of_two_cheapest
        else:
            return money