class Solution:
    def _get_next(self, n: int) -> int:
        total_sum = 0
        while n > 0:
            digit = n % 10
            total_sum += digit * digit
            n //= 10
        return total_sum

    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = self._get_next(n)
        return n == 1