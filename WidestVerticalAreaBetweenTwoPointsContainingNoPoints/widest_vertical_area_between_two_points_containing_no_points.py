class Solution:
    def maxWidthOfVerticalArea(self, points: list[list[int]]) -> int:
        x_coords = []
        for point in points:
            x_coords.append(point[0])

        x_coords.sort()

        max_width = 0

        for i in range(1, len(x_coords)):
            current_width = x_coords[i] - x_coords[i-1]
            if current_width > max_width:
                max_width = current_width
        
        return max_width