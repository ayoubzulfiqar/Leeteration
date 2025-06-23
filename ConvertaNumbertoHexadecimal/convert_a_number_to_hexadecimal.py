def toHex(num: int) -> str:
    if num == 0:
        return "0"

    hex_chars = "0123456789abcdef"
    result_chars = []

    if num < 0:
        num += 2**32

    while num > 0:
        remainder = num % 16
        result_chars.append(hex_chars[remainder])
        num //= 16
    
    result_chars.reverse()
    return "".join(result_chars)