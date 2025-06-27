class Solution:
    def findMissingAndRepeatedValues(self, grid: list[list[int]]) -> list[int]:
        n = len(grid)
        total_elements = n * n
        
        counts = [0] * (total_elements + 1)
        
        repeated_num = -1
        
        for r in range(n):
            for c in range(n):
                num = grid[r][c]
                counts[num] += 1
                if counts[num] == 2:
                    repeated_num = num
        
        missing_num = -1
        for i in range(1, total_elements + 1):
            if counts[i] == 0:
                missing_num = i
                break
                
        return [repeated_num, missing_num]