class Solution:
    def isFascinating(self, n: int) -> bool:
        n2 = 2 * n
        n3 = 3 * n
        concatenated_str = str(n) + str(n2) + str(n3)
        
        target_digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        
        sorted_concatenated_chars = sorted(list(concatenated_str))
        
        return sorted_concatenated_chars == target_digits