class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        perimeter = 0
        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    perimeter += 4
                    
                    # Check up neighbor
                    if r > 0 and grid[r-1][c] == 1:
                        perimeter -= 1
                    # Check down neighbor
                    if r < rows - 1 and grid[r+1][c] == 1:
                        perimeter -= 1
                    # Check left neighbor
                    if c > 0 and grid[r][c-1] == 1:
                        perimeter -= 1
                    # Check right neighbor
                    if c < cols - 1 and grid[r][c+1] == 1:
                        perimeter -= 1
        return perimeter