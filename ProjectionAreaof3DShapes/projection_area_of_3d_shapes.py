class Solution:
    def projectionArea(self, grid: list[list[int]]) -> int:
        n = len(grid)
        
        xy_area = 0
        zx_area = 0 # Sum of maximums of each row
        yz_area = 0 # Sum of maximums of each column
        
        # Initialize an array to store the maximum height found for each column
        # This is necessary because we iterate row by row, but need column-wise maximums
        col_maxes = [0] * n 
        
        for i in range(n):
            # For ZX-plane (side view), we need the maximum height in the current row
            row_max = 0
            for j in range(n):
                # For XY-plane (top view), if there's any cube, it contributes 1 unit area
                if grid[i][j] > 0:
                    xy_area += 1
                
                # Update the maximum height for the current row (for ZX-plane)
                row_max = max(row_max, grid[i][j])
                
                # Update the maximum height for the current column (for YZ-plane)
                col_maxes[j] = max(col_maxes[j], grid[i][j])
            
            # Add the maximum height of the current row to the total ZX-plane area
            zx_area += row_max
            
        # After iterating through all rows, col_maxes contains the maximum height for each column.
        # Sum these maximums to get the total YZ-plane area.
        yz_area = sum(col_maxes)
        
        # The total projection area is the sum of areas from all three planes
        return xy_area + yz_area + zx_area