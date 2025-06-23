import math

class Solution:
    def constructRectangle(self, area: int) -> list[int]:
        
        width = int(math.sqrt(area))
        
        while area % width != 0:
            width -= 1
            
        length = area // width
        
        return [length, width]