class Solution:
    def rowAndMaximumOnes(self, mat: list[list[int]]) -> list[int]:
        max_ones_count = -1
        max_ones_row_index = -1

        for i in range(len(mat)):
            current_ones = mat[i].count(1)
            
            if current_ones > max_ones_count:
                max_ones_count = current_ones
                max_ones_row_index = i
        
        return [max_ones_row_index, max_ones_count]