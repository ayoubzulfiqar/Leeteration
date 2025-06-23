class Solution:
    def imageSmoother(self, img: list[list[int]]) -> list[list[int]]:
        m = len(img)
        n = len(img[0])
        
        smoothed_img = [[0] * n for _ in range(m)]
        
        for r in range(m):
            for c in range(n):
                total_sum = 0
                count = 0
                
                # Iterate over the 3x3 neighborhood
                for dr in range(-1, 2):
                    for dc in range(-1, 2):
                        nr, nc = r + dr, c + dc
                        
                        # Check if the neighbor is within bounds
                        if 0 <= nr < m and 0 <= nc < n:
                            total_sum += img[nr][nc]
                            count += 1
                
                # Calculate the floored average
                smoothed_img[r][c] = total_sum // count
                
        return smoothed_img