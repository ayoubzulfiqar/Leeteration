pick = 6

def guess(num: int) -> int:
    if num > pick:
        return -1
    elif num < pick:
        return 1
    else:
        return 0

class Solution:
    def guessNumber(self, n: int) -> int:
        low = 1
        high = n

        while low <= high:
            mid = low + (high - low) // 2
            result = guess(mid)

            if result == 0:
                return mid
            elif result == -1:
                high = mid - 1
            else:
                low = mid + 1
        return -1