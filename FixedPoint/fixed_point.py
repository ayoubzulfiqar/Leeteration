class Solution:
    def findFixedPoint(self, arr: list[int]) -> int:
        """
        Finds the smallest index i such that arr[i] == i in a sorted array.
        Returns -1 if no such index exists.
        """
        low = 0
        high = len(arr) - 1
        ans = -1

        while low <= high:
            mid = low + (high - low) // 2

            if arr[mid] == mid:
                ans = mid
                # Found a fixed point, but try to find an even smaller one on the left
                high = mid - 1
            elif arr[mid] < mid:
                # The value at mid is too small compared to its index.
                # Since the array is sorted, we need to go right to find a larger value
                # that might eventually match its index.
                low = mid + 1
            else: # arr[mid] > mid
                # The value at mid is too large compared to its index.
                # Since the array is sorted, we need to go left to find a smaller value
                # that might eventually match its index.
                high = mid - 1
        return ans