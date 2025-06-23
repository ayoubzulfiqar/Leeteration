class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        triangle = []

        if numRows == 0:
            return triangle

        # First row is always [1]
        triangle.append([1])

        for row_num in range(1, numRows):
            current_row = [1]
            prev_row = triangle[row_num - 1]

            # Calculate intermediate elements
            for j in range(1, len(prev_row)):
                current_row.append(prev_row[j - 1] + prev_row[j])
            
            # Last element is always 1
            current_row.append(1)
            triangle.append(current_row)

        return triangle