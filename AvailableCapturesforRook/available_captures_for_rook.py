class Solution:
    def numRookCaptures(self, board: list[list[str]]) -> int:
        rook_row, rook_col = -1, -1
        for r in range(8):
            for c in range(8):
                if board[r][c] == 'R':
                    rook_row, rook_col = r, c
                    break
            if rook_row != -1:
                break

        captures = 0
        
        # Define directions: right, left, down, up
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for dr, dc in directions:
            curr_row, curr_col = rook_row + dr, rook_col + dc
            while 0 <= curr_row < 8 and 0 <= curr_col < 8:
                if board[curr_row][curr_col] == 'p':
                    captures += 1
                    break 
                elif board[curr_row][curr_col] == 'B':
                    break 
                
                curr_row += dr
                curr_col += dc
                
        return captures