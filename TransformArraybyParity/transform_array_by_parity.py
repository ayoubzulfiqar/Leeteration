class Solution:
    def transformArrayByParity(self, nums: list[int]) -> list[int]:
        transformed_nums = []
        for num in nums:
            if num % 2 == 0:
                transformed_nums.append(0)
            else:
                transformed_nums.append(1)
        transformed_nums.sort()
        return transformed_nums