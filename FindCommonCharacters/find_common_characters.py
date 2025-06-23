class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        min_freq = [0] * 26
        
        for char_code in words[0]:
            min_freq[ord(char_code) - ord('a')] += 1
        
        for i in range(1, len(words)):
            current_word_freq = [0] * 26
            for char_code in words[i]:
                current_word_freq[ord(char_code) - ord('a')] += 1
            
            for j in range(26):
                min_freq[j] = min(min_freq[j], current_word_freq[j])
                
        result = []
        for j in range(26):
            char = chr(ord('a') + j)
            count = min_freq[j]
            result.extend([char] * count)
            
        return result