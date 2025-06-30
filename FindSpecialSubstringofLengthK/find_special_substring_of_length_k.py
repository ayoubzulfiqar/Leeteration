class Solution:
    def findSpecialSubstring(self, s: str, k: int) -> bool:
        n = len(s)

        for i in range(n - k + 1):
            substring = s[i : i + k]

            if not (substring[0] * k == substring):
                continue

            if i > 0:
                if s[i - 1] == substring[0]:
                    continue

            if i + k < n:
                if s[i + k] == substring[0]:
                    continue

            return True

        return False