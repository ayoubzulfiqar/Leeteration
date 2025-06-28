def solution(x: int) -> int:
    """
    Checks if an integer x is a Harshad number.

    An integer divisible by the sum of its digits is said to be a Harshad number.

    Args:
        x: An integer.

    Returns:
        The sum of the digits of x if x is a Harshad number, otherwise, -1.
    """
    sum_of_digits = 0
    temp_x = x
    while temp_x > 0:
        sum_of_digits += temp_x % 10
        temp_x //= 10

    if x % sum_of_digits == 0:
        return sum_of_digits
    else:
        return -1

```