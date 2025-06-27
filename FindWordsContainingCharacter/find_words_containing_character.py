class Solution:
    def findWordsContaining(self, words: list[str], x: str) -> list[int]:
        result_indices = []
        for i, word in enumerate(words):
            if x in word:
                result_indices.append(i)
        return result_indices