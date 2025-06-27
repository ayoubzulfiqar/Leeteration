class Solution:
    def areSimilar(self, mat: list[list[int]], k: int) -> bool:
        m = len(mat)
        n = len(mat[0])

        original_mat = [row[:] for row in mat]

        effective_k = k % n

        if effective_k == 0:
            return True

        modified_mat = [row[:] for row in mat]

        for i in range(m):
            current_row = modified_mat[i]
            if i % 2 == 0:
                modified_mat[i] = current_row[effective_k:] + current_row[:effective_k]
            else:
                modified_mat[i] = current_row[n - effective_k:] + current_row[:n - effective_k]
        
        return modified_mat == original_mat