class Solution:
    def surfaceArea(self, grid: list[list[int]]) -> int:
        n = len(grid)
        total_surface_area = 0

        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]

        for r in range(n):
            for c in range(n):
                height = grid[r][c]

                if height == 0:
                    continue

                total_surface_area += 2

                for i in range(4):
                    nr, nc = r + dr[i], c + dc[i]

                    neighbor_height = 0
                    if 0 <= nr < n and 0 <= nc < n:
                        neighbor_height = grid[nr][nc]

                    total_surface_area += max(0, height - neighbor_height)

        return total_surface_area