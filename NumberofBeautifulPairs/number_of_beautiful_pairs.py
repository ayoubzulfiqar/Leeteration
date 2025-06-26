import math

class Solution:
    def countBeautifulPairs(self, nums: list[int]) -> int:
        count = 0
        n = len(nums)

        for i in range(n):
            first_digit_i = int(str(nums[i])[0])

            for j in range(i + 1, n):
                last_digit_j = nums[j] % 10

                if math.gcd(first_digit_i, last_digit_j) == 1:
                    count += 1
        return count