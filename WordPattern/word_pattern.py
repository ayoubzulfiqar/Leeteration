class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')

        if len(pattern) != len(words):
            return False

        char_to_word = {}
        word_to_char = {}

        for i in range(len(pattern)):
            char = pattern[i]
            word = words[i]

            if char in char_to_word:
                if char_to_word[char] != word:
                    return False
            else:
                # If char is new, word must also be new (not mapped to another char)
                if word in word_to_char:
                    return False
            
            if word in word_to_char:
                if word_to_char[word] != char:
                    return False
            else:
                # If word is new, char must also be new (not mapped to another word)
                if char in char_to_word: # This check is redundant with the first else block
                    pass # Already handled, or implies consistency
            
            # Establish or confirm the mapping
            char_to_word[char] = word
            word_to_char[word] = char
        
        return True