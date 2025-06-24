class Solution:
    def sortString(self, s: str) -> str:
        counts = [0] * 26
        for char_code in s:
            counts[ord(char_code) - ord('a')] += 1

        result_chars = []
        n = len(s)

        while len(result_chars) < n:
            # Ascending pass: pick smallest, then smallest greater than last, etc.
            # This is achieved by iterating through the alphabet from 'a' to 'z'
            # and picking any character that is available (count > 0).
            for i in range(26):
                if counts[i] > 0:
                    result_chars.append(chr(ord('a') + i))
                    counts[i] -= 1

            # Descending pass: pick largest, then largest smaller than last, etc.
            # This is achieved by iterating through the alphabet from 'z' to 'a'
            # and picking any character that is available (count > 0).
            for i in range(25, -1, -1):
                if counts[i] > 0:
                    result_chars.append(chr(ord('a') + i))
                    counts[i] -= 1
        
        return "".join(result_chars)