class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balanced_strings_count = 0
        balance_tracker = 0

        for char in s:
            if char == 'L':
                balance_tracker -= 1
            else:  # char == 'R'
                balance_tracker += 1
            
            if balance_tracker == 0:
                balanced_strings_count += 1
                
        return balanced_strings_count