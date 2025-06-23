class Solution:
    def indexPairs(self, text: str, words: list[str]) -> list[list[int]]:
        result = []
        n = len(text)

        for word in words:
            len_word = len(word)
            for i in range(n - len_word + 1):
                if text[i : i + len_word] == word:
                    result.append([i, i + len_word - 1])

        result.sort()
        return result