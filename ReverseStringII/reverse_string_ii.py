class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        a = list(s)
        n = len(a)

        for i in range(0, n, 2 * k):
            left = i
            right = min(i + k - 1, n - 1)

            while left < right:
                a[left], a[right] = a[right], a[left]
                left += 1
                right -= 1
        
        return "".join(a)