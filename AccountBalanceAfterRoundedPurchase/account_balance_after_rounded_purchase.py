class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        initial_balance = 100
        
        remainder = purchaseAmount % 10
        
        if remainder >= 5:
            roundedAmount = (purchaseAmount // 10) * 10 + 10
        else:
            roundedAmount = (purchaseAmount // 10) * 10
            
        final_balance = initial_balance - roundedAmount
        
        return final_balance