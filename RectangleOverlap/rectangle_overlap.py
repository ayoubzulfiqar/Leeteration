class Solution:
    def isRectangleOverlap(self, rec1: list[int], rec2: list[int]) -> bool:
        ax1, ay1, ax2, ay2 = rec1
        bx1, by1, bx2, by2 = rec2

        x_overlap = (ax1 < bx2 and bx1 < ax2)
        y_overlap = (ay1 < by2 and by1 < ay2)

        return x_overlap and y_overlap