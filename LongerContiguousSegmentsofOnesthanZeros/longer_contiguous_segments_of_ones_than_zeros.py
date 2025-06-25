```python
def check_zero_one(s: str) -> bool:
    """Given a binary string s, return true if the longest contiguous segment of 1's is strictly longer than the longest contiguous segment of 0's in s, or return false otherwise.

    For example, in s = "110100010" the longest continuous segment of 1s has length 2, and the longest continuous segment of 0s has length 3.
    Note that if there are no 0's, then the longest continuous segment of 0's is considered to have a length 0. The same applies if there is no 1's.

    Example 1:
    Input: s = "1101"
    Output: true
    Explanation:
    The longest contiguous segment of 1s has length 2: "1101"
    The longest contiguous segment of 0s has length 1: "1101"
    The segment of 1s is longer, so return true.

    Example 2:
    Input: s = "111000"
    Output: false
    Explanation:
    The longest contiguous segment of 1s has length 3: "111000"
    The longest contiguous segment of 0s has length 3: "111000"
    The segment of 1s is not longer, so return false.

    Example 3:
    Input: s = "110100010"
    Output: false
    Explanation:
    The longest contiguous segment of 1s has length 2: "110100010"
    The longest contiguous segment of 0s has length 3: "110100010"
    The segment of 1s is not longer, so return false.

    Constraints:
    1 <= s.length <= 100
    s[i] is either '0' or '1'.
    """
    max_one = 0
    max_zero = 0
    count_one = 0
    count_zero = 0
    for i in range(len(s)):
        if s[i] == '1':
            count_one += 1
            count_zero = 0
        else:
            count_zero += 1
            count_one = 0
        max_one = max(max_one, count_one)
        max_zero = max(max_zero, count_zero)
    return max_one > max_zero
```