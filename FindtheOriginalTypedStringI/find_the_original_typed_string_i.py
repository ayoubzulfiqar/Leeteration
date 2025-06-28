class Solution:
    def countPossibleOriginalStrings(self, word: str) -> int:
        n = len(word)
        
        total_possible_strings = 1 

        i = 0
        while i < n:
            current_char = word[i]
            j = i
            while j < n and word[j] == current_char:
                j += 1
            
            group_length = j - i
            
            total_possible_strings += (group_length - 1)
            
            i = j
            
        return total_possible_strings