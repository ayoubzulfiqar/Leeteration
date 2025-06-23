class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> list[list[int]]:
        cells_with_distance = []
        for r in range(rows):
            for c in range(cols):
                distance = abs(r - rCenter) + abs(c - cCenter)
                cells_with_distance.append((distance, [r, c]))

        cells_with_distance.sort()

        result = []
        for distance, cell in cells_with_distance:
            result.append(cell)
            
        return result