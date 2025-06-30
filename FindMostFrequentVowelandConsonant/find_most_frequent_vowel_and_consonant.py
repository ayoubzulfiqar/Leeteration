class Solution:
    def solve(self, s: str) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        vowel_freq = {}
        consonant_freq = {}
        
        for char in s:
            if char in vowels:
                vowel_freq[char] = vowel_freq.get(char, 0) + 1
            else:
                consonant_freq[char] = consonant_freq.get(char, 0) + 1
                
        max_vowel_freq = 0
        if vowel_freq:
            max_vowel_freq = max(vowel_freq.values())
            
        max_consonant_freq = 0
        if consonant_freq:
            max_consonant_freq = max(consonant_freq.values())
            
        return max_vowel_freq + max_consonant_freq