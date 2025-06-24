import bisect

class Solution:
    def findSpecialInteger(self, arr: list[int]) -> int:
        n = len(arr)
        
        if n == 1:
            return arr[0]

        threshold_count = n // 4
        
        candidates = [arr[0], arr[n // 4], arr[n // 2], arr[3 * n // 4]]
        
        for candidate in candidates:
            left_idx = bisect.bisect_left(arr, candidate)
            right_idx = bisect.bisect_right(arr, candidate)
            
            if (right_idx - left_idx) > threshold_count:
                return candidate