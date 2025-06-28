import collections

class Solution:
    def minimumBoxes(self, apple: list[int], capacity: list[int]) -> int:
        total_apples = sum(apple)
        capacity.sort(reverse=True)
        
        current_capacity = 0
        boxes_used = 0
        
        for cap in capacity:
            current_capacity += cap
            boxes_used += 1
            if current_capacity >= total_apples:
                return boxes_used
        
        return boxes_used # Should always be reached due to problem constraints guaranteeing possibility