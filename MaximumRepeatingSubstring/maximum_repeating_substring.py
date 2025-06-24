class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        k = 0
        test_string = word
        while test_string in sequence:
            k += 1
            test_string = word * (k + 1)
        return k