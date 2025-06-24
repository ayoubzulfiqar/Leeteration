class Solution:
    def dietPlanPerformance(self, calories: list[int], k: int, lower: int, upper: int) -> int:
        points = 0
        n = len(calories)

        current_sum = sum(calories[0:k])

        if current_sum < lower:
            points -= 1
        elif current_sum > upper:
            points += 1

        for i in range(k, n):
            current_sum = current_sum - calories[i - k] + calories[i]
            
            if current_sum < lower:
                points -= 1
            elif current_sum > upper:
                points += 1
        
        return points