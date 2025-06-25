```python
def longestNiceSubstring(s: str) -> str:
    """
    Given a string s, return the longest substring of s that is nice.
    A string s is nice if, for every letter of the alphabet that s contains, it appears both in uppercase and lowercase.
    For example, "abABB" is nice because 'A' and 'a' appear, and 'B' and 'b' appear. However, "abA" is not because 'b' appears, but 'B' does not.
    If there are multiple, return the substring of the earliest occurrence. If there are none, return an empty string.

    Constraints:
    1 <= s.length <= 100
    s consists of uppercase and lowercase English letters.
    """

    def is_nice(sub):
        chars = set(sub)
        for char in chars:
            if 'a' <= char <= 'z':
                if char.upper() not in sub:
                    return False
            elif 'A' <= char <= 'Z':
                if char.lower() not in sub:
                    return False
        return True

    longest = ""
    for i in range(len(s)):
        for j in range(i, len(s)):
            sub = s[i:j+1]
            if is_nice(sub):
                if len(sub) > len(longest):
                    longest = sub
    return longest
```