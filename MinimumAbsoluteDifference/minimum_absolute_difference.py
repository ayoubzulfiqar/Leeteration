class Solution:
    def minimumAbsoluteDifference(self, arr: list[int]) -> list[list[int]]:
        arr.sort()

        min_diff = float('inf')
        
        for i in range(len(arr) - 1):
            current_diff = arr[i+1] - arr[i]
            if current_diff < min_diff:
                min_diff = current_diff
        
        result = []
        for i in range(len(arr) - 1):
            if arr[i+1] - arr[i] == min_diff:
                result.append([arr[i], arr[i+1]])
                
        return result