class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        for i in range(len(nums)):
            index_to_mark = abs(nums[i]) - 1
            if nums[index_to_mark] > 0:
                nums[index_to_mark] *= -1

        disappeared_numbers = []
        for i in range(len(nums)):
            if nums[i] > 0:
                disappeared_numbers.append(i + 1)

        return disappeared_numbers