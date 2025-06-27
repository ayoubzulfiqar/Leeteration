class Solution:
    def distributeMoney(self, money: int, children: int) -> int:
        # Iterate from the maximum possible number of children receiving 8 dollars
        # down to 0. The first valid k found is the maximum.
        # k represents the number of children who receive exactly 8 dollars.
        for k in range(children, -1, -1):
            money_for_8_dollar_children = k * 8
            remaining_money = money - money_