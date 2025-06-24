class Solution:
    def average(self, salary: list[int]) -> float:
        min_s = min(salary)
        max_s = max(salary)
        total_sum = sum(salary)
        
        sum_excluding_min_max = total_sum - min_s - max_s
        count_excluding_min_max = len(salary) - 2
        
        return sum_excluding_min_max / count_excluding_min_max