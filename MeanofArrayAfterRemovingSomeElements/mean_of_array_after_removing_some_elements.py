class Solution:
    def trimMean(self, arr: list[int]) -> float:
        n = len(arr)
        remove_count = n // 20  # 5% of n
        
        arr.sort()
        
        # Slice the array to remove the smallest 5% and largest 5%
        # The elements to keep are from index `remove_count` up to `n - remove_count - 1`
        trimmed_arr = arr[remove_count : n - remove_count]
        
        total_sum = sum(trimmed_arr)
        remaining_count = len(trimmed_arr)
        
        return total_sum / remaining_count