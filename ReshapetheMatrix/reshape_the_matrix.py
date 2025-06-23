class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        m = len(mat)
        n = len(mat[0])

        if m * n != r * c:
            return mat

        flattened_elements = []
        for row in mat:
            for element in row:
                flattened_elements.append(element)

        reshaped_matrix = []
        element_index = 0
        for _ in range(r):
            current_row = []
            for _ in range(c):
                current_row.append(flattened_elements[element_index])
                element_index += 1
            reshaped_matrix.append(current_row)

        return reshaped_matrix