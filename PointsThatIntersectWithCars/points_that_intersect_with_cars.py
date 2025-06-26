class Solution:
    def numberOfPoints(self, nums: list[list[int]]) -> int:
        covered_points = set()
        for start, end in nums:
            for point in range(start, end + 1):
                covered_points.add(point)
        return len(covered_points)