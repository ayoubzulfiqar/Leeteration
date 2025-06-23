_first_bad_version_for_testing = 1

def isBadVersion(version: int) -> bool:
    return version >= _first_bad_version_for_testing

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        first_bad = n

        while left <= right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                first_bad = mid
                right = mid - 1
            else:
                left = mid + 1

        return first_bad