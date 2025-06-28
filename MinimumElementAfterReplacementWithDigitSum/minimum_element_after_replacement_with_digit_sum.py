class Solution:
    def minimumElementAfterReplacement(self, nums: list[int]) -> int:
        def sum_digits(n: int) -> int:
            s = 0
            while n > 0:
                s += n % 10
                n //= 10
            return s

        transformed_nums = []
        for num in nums:
            transformed_nums.append(sum_digits(num))

        return min(transformed_nums)