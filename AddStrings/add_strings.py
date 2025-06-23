class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        result = []
        i = len(num1) - 1
        j = len(num2) - 1
        carry = 0

        while i >= 0 or j >= 0 or carry:
            digit1 = int(num1[i]) if i >= 0 else 0
            digit2 = int(num2[j]) if j >= 0 else 0

            current_sum = digit1 + digit2 + carry
            carry = current_sum // 10
            digit_to_add = current_sum % 10

            result.append(str(digit_to_add))

            i -= 1
            j -= 1
        
        return "".join(result[::-1])