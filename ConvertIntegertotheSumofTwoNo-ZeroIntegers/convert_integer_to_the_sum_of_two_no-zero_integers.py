class Solution:
    def getNoZeroIntegers(self, n: int) -> list[int]:
        def _is_no_zero(num: int) -> bool:
            return '0' not in str(num)

        for a in range(1, n):
            b = n - a
            if _is_no_zero(a) and _is_no_zero(b):
                return [a, b]

        return [] # Should not be reached based on problem constraints