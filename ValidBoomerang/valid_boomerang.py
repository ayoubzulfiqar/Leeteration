class Solution:
    def isBoomerang(self, points: list[list[int]]) -> bool:
        x1, y1 = points[0]
        x2, y2 = points[1]
        x3, y3 = points[2]

        # Check if any two points are identical (not distinct)
        if (x1 == x2 and y1 == y2) or \
           (x1 == x3 and y1 == y3) or \
           (x2 == x3 and y2 == y3):
            return False

        # Check for collinearity using the cross-product method.
        # Three points (x1, y1), (x2, y2), (x3, y3) are collinear if
        # (y2 - y1) * (x3 - x2) == (y3 - y2) * (x2 - x1)
        # If they are collinear, it's not a boomerang.
        if (y2 - y1) * (x3 - x2) == (y3 - y2) * (x2 - x1):
            return False
        
        # If all points are distinct and not collinear, it's a boomerang.
        return True