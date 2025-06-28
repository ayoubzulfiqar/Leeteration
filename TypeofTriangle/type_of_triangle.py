class Solution:
    def triangleType(self, nums: list[int]) -> str:
        a, b, c = nums[0], nums[1], nums[2]

        if not (a + b > c and a + c > b and b + c > a):
            return "none"

        if a == b and b == c:
            return "equilateral"
        elif a == b or a == c or b == c:
            return "isosceles"
        else:
            return "scalene"