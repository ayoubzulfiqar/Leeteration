class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        count_even_digits = 0
        for num in nums:
            num_str = str(num)
            if len(num_str) % 2 == 0:
                count_even_digits += 1
        return count_even_digits