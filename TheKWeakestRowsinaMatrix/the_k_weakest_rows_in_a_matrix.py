class Solution:
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
        row_strengths = []
        for i, row in enumerate(mat):
            soldiers = sum(row)
            row_strengths.append((soldiers, i))

        row_strengths.sort()

        result = []
        for i in range(k):
            result.append(row_strengths[i][1])
            
        return result