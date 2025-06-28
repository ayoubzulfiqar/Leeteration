class Solution:
    def encryptString(self, s: str, k: int) -> str:
        n = len(s)
        encrypted_chars = [''] * n
        for i in range(n):
            new_index = (i + k) % n
            encrypted_chars[i] = s[new_index]
        return "".join(encrypted_chars)