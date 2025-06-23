from typing import List

class Solution:
    def is_self_dividing(self, num: int) -> bool:
        temp_num = num
        while temp_num > 0:
            digit = temp_num % 10
            if digit == 0:
                return False
            if num % digit != 0:
                return False
            temp_num //= 10
        return True

    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        for num in range(left, right + 1):
            if self.is_self_dividing(num):
                result.append(num)
        return result