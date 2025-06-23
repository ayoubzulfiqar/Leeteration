class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"

        is_negative = False
        if num < 0:
            is_negative = True
            num = -num

        result_digits = []
        while num > 0:
            remainder = num % 7
            result_digits.append(str(remainder))
            num //= 7

        base7_str = "".join(result_digits[::-1])

        if is_negative:
            return "-" + base7_str
        else:
            return base7_str