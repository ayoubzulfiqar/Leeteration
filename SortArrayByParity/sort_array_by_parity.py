class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        even_nums = []
        odd_nums = []
        for num in nums:
            if num % 2 == 0:
                even_nums.append(num)
            else:
                odd_nums.append(num)
        return even_nums + odd_nums