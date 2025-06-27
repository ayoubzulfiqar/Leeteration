class Solution:
    def findCommonElements(self, nums1: list[int], nums2: list[int]) -> list[int]:
        answer1 = 0
        answer2 = 0

        set_nums2 = set(nums2)
        for num in nums1:
            if num in set_nums2:
                answer1 += 1

        set_nums1 = set(nums1)
        for num in nums2:
            if num in set_nums1:
                answer2 += 1

        return [answer1, answer2]