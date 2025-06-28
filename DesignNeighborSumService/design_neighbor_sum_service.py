class NeighborSum:
    def __init__(self, grid: list[list[int]]):
        self.grid = grid
        self.n = len(grid)
        self.val_to_coords = {}
        for r in range(self.n):
            for c in range(self.n):
                self.val_to_coords[self.grid[r][c]] = (r, c)

    def adjacentSum(self, value: int) -> int:
        r, c = self.val_to_coords[value]
        total_sum = 0
        
        # Possible adjacent directions: up, down, left, right
        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]
        
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            
            if 0 <= nr < self.n and 0 <= nc < self.n:
                total_sum += self.grid[nr][nc]
                
        return total_sum

    def diagonalSum(self, value: int) -> int:
        r, c = self.val_to_coords[value]
        total_sum = 0
        
        # Possible diagonal directions: top-left, top-right, bottom-left, bottom-right
        dr = [-1, -1, 1, 1]
        dc = [-1, 1, -1, 1]
        
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            
            if 0 <= nr < self.n and 0 <= nc < self.n:
                total_sum += self.grid[nr][nc]
                
        return total_sum