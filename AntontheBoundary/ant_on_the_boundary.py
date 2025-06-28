class Solution:
    def antOnTheBoundary(self, nums: list[int]) -> int:
        current_position = 0
        boundary_returns = 0
        for move in nums:
            current_position += move
            if current_position == 0:
                boundary_returns += 1
        return boundary_returns