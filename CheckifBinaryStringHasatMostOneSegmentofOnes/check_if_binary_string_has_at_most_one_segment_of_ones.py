```python
def check_if_binary_string_has_at_most_one_segment_of_ones(s: str) -> bool:
    """
    Given a binary string s without leading zeros, return true if s contains at most one contiguous segment of ones.
    Otherwise, return false.
    Example 1:
    Input: s = "1001"
    Output: false
    Explanation: The ones do not form a contiguous segment.
    Example 2:
    Input: s = "110"
    Output: true
    Constraints:
    1 <= s.length <= 100
    s[i] is either '0' or '1'.
    s[0] is '1'.
    """
    count = 0
    for i in range(1, len(s)):
        if s[i] == '1' and s[i - 1] == '0':
            count += 1
    return count == 0
```