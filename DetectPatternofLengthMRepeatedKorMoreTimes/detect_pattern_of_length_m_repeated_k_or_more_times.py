class Solution:
    def containsPattern(self, arr: list[int], m: int, k: int) -> bool:
        n = len(arr)
        
        for i in range(n - m * k + 1):
            current_pattern = arr[i : i + m]
            
            repetitions = 1
            
            j = i + m
            
            while j + m <= n:
                next_block = arr[j : j + m]
                
                if next_block == current_pattern:
                    repetitions += 1
                    j += m
                else:
                    break
            
            if repetitions >= k:
                return True
                
        return False