class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        str1 = "".join(word1)
        str2 = "".join(word2)
        return str1 == str2