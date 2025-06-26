class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        total_sum_up_to_n = n * (n + 1) // 2
        
        k = n // m
        
        sum_divisible_by_m = m * (k * (k + 1) // 2)
        
        return total_sum_up_to_n - 2 * sum_divisible_by_m