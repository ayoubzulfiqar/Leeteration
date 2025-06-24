import collections

class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        available_chars_count = collections.Counter(chars)
        
        total_length = 0
        
        for word in words:
            word_chars_count = collections.Counter(word)
            
            is_good_word = True
            for char, count in word_chars_count.items():
                if available_chars_count[char] < count:
                    is_good_word = False
                    break
            
            if is_good_word:
                total_length += len(word)
                
        return total_length