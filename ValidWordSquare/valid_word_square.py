class Solution:
    def validWordSquare(self, words: list[str]) -> bool:
        n = len(words)

        for i in range(n):
            if len(words[i]) > n:
                return False

        for i in range(n):
            for j in range(n):
                char1 = words[i][j] if j < len(words[i]) else None
                char2 = words[j][i] if i < len(words[j]) else None

                if char1 != char2:
                    return False
        
        return True