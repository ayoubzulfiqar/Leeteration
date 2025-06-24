import bisect

class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        low = 1
        high = arr[-1] + k 
        ans = high

        while low <= high:
            mid = low +