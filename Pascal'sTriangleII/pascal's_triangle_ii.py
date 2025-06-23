class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        row = [0] * (rowIndex + 1)
        row[0] = 1

        for i in range(1, rowIndex + 1):
            row[i] = 1
            for j in range(i - 1, 0, -1):
                row[j] = row[j] + row[j-1]
        
        return row