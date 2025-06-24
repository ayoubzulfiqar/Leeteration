class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        distance_value_count = 0
        for num1 in arr1:
            is_far_enough = True
            for num2 in arr2:
                if abs(num1 - num2) <= d:
                    is_far_enough = False
                    break
            if is_far_enough:
                distance_value_count += 1
        return distance_value_count