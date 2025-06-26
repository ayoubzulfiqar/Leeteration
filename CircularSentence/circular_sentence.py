class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split(' ')
        n = len(words)

        for i in range(n):
            current_word = words[i]
            next_word_index = (i + 1) % n
            next_word = words[next_word_index]

            if current_word[-1] != next_word[0]:
                return False
        
        return True