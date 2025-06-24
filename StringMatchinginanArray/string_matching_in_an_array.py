class Solution:
    def stringMatching(self, words: list[str]) -> list[str]:
        result_set = set()
        n = len(words)
        for i in range(n):
            for j in range(n):
                if i != j and words[i] in words[j]:
                    result_set.add(words[i])
        return list(result_set)