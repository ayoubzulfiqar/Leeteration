```python
def is_decomposable(s: str) -> bool:
    """
    Given a string s, check if it can be decomposed into value-equal substrings.
    A value-equal substring contains only one type of character.
    For example: "111", "00000", "abcabcabc".
    A string s can be decomposed into value-equal substrings if the length of each substring is a multiple of 3.
    For example: "111222" can be decomposed into "111" and "222".
    "111222333" can be decomposed into "111", "222", and "333".
    "11122233" cannot be decomposed into value-equal substrings because "33" is not a multiple of 3.
    "111222333444" can be decomposed into "111", "222", "333", and "444".

    s = "111222"
    is_decomposable(s) == True

    s = "11122233"
    is_decomposable(s) == False

    s = "111222333444"
    is_decomposable(s) == True

    s = "11122233344"
    is_decomposable(s) == False

    s = "1112223334445"
    is_decomposable(s) == False
    """
    if not s:
        return True

    i = 0
    while i < len(s):
        j = i
        while j < len(s) and s[i] == s[j]:
            j += 1

        if (j - i) % 3 != 0:
            return False

        i = j

    return True
```