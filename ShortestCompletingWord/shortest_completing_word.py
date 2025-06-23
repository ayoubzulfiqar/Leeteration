import collections

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: list[str]) -> str:
        lp_char_counts = collections.Counter()
        for char in licensePlate:
            if 'a' <= char <= 'z':
                lp_char_counts[char] += 1
            elif 'A' <= char <= 'Z':
                lp_char_counts[char.lower()] += 1
        
        shortest_word = None
        min_length = float('inf')
        
        for word in words:
            word_char_counts = collections.Counter(word)
            
            is_completing = True
            for char, count_lp in lp_char_counts.items():
                if word_char_counts[char] < count_lp:
                    is_completing = False
                    break
            
            if is_completing:
                if len(word) < min_length:
                    min_length = len(word)
                    shortest_word = word
        
        return shortest_word