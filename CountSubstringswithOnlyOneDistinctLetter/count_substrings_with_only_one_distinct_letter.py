class Solution:
    def countLetters(self, s: str) -> int:
        total_count = 0
        current_length = 0
        prev_char = '' 

        for char in s:
            if char == prev_char:
                current_length += 1
            else:
                current_length = 1
            
            total_count += current_length
            prev_char = char
        
        return total_count