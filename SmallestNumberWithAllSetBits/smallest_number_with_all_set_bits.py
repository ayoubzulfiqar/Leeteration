def smallest_number_with_all_set_bits(n: int) -> int:
    """
    Returns the smallest number x greater than or equal to n,
    such that the binary representation of x contains only set bits.
    """
    x = 1  # Start with the smallest number having all set bits (binary "1")
    while x < n:
        # Generate the next number with all set bits.
        # If x is 2^k - 1, the next one is 2^(k+1) - 1.
        # This can be achieved by x = x * 2 + 1, or using bitwise operations:
        # Shift x left by 1 (equivalent to x * 2) and then set the least significant bit to 1.
        x = (x << 1) | 1
    return x