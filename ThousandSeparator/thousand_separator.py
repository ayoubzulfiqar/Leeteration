class Solution:
    def thousandSeparator(self, n: int) -> str:
        s = "{:,}".format(n)
        return s.replace(",", ".")