class Solution:
    def minOperations(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        total_operations = 0
        
        for j in range(n):  # Iterate through each column
            # current_val_in_column tracks the value the previous cell in the column
            # effectively became after any necessary operations.
            # This determines the minimum required value for the current cell.
            current_val_in_column = grid[0][j] 
            
            for i in range(1, m):  # Iterate through rows starting from the second row
                # The current cell grid[i][j] must be strictly greater than
                # the effective value of the cell above it (current_val_in_column).
                # So, grid[i][j] must be at least current_val_in_column + 1.
                required_val = current_val_in_column + 1
                
                if grid[i][j] < required_val:
                    # If grid[i][j] is less than the required value, operations are needed.
                    operations_needed = required_val - grid[i][j]
                    total_operations += operations_needed
                    
                    # Update current_val_in_column to the new value grid[i][j] effectively became.
                    # This new value will be used for the comparison with the next cell in the column.
                    current_val_in_column = required_val
                else:
                    # If grid[i][j] is already greater than or equal to the required value,
                    # no operations are needed for this specific cell.
                    # Update current_val_in_column to the actual value of grid[i][j],
                    # as it is already valid and will serve as the base for the next comparison.
                    current_val_in_column = grid[i][j]
                    
        return total_operations