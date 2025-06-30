class Solution:
    def checkDigits(self, s: str) -> bool:
        while len(s) > 2:
            next_s_chars = []
            for i in range(len(s) - 1):
                digit1 = int(s[i])
                digit2 = int(s[i+1])
                new_digit = (digit1 + digit2) % 10
                next_s_chars.append(str(new_digit))
            s = "".join(next_s_chars)
        
        return s[0] == s[1]