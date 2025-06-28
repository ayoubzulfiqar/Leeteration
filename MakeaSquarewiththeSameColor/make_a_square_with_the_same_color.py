class Solution:
    def makesquare(self, grid: list[list[str]]) -> bool:
        def check_square_possibility(cells: list[str]) -> bool:
            count_b = cells.count('B')
            count_w = cells.count('W')
            return count_b <= 1 or count_w <= 1

        for r in range(2):
            for c in range(2):
                current_square_cells = [
                    grid[r][c],
                    grid[r][c+1],
                    grid[r+1][c],
                    grid[r+1][c+1]
                ]
                if check_square_possibility(current_square_cells):
                    return True
        
        return False