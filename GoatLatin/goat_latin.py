class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        words = sentence.split()
        vowels = {'a', 'e', 'i', 'o', 'u'}
        result_words = []

        for i, word in enumerate(words):
            first_char = word[0]
            
            if first_char.lower() in vowels:
                transformed_word = word + "ma"
            else:
                transformed_word = word[1:] + first_char + "ma"
            
            transformed_word += 'a' * (i + 1)
            result_words.append(transformed_word)
        
        return " ".join(result_words)