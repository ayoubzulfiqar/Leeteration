class Solution:
    def tictactoe(self, moves: list[list[int]]) -> str:
        board = [[' ' for _ in range(3)] for _ in range(3)]

        def check_winner(current_board):
            # Check rows
            for r in range(3):
                if current_board[r][0] == current_board[r][1] == current_board[r][2] and current_board[r][0] != ' ':
                    return current_board[r][0]
            
            # Check columns
            for c in range(3):
                if current_board[0][c] == current_board[1][c] == current_board[2][c] and current_board[0][c] != ' ':
                    return current_board[0][c]
            
            # Check diagonals
            if current_board[0][0] == current_board[1][1] == current_board[2][2] and current_board[0][0] != ' ':
                return current_board[0][0]
            if current_board[0][2] == current_board[1][1] == current_board[2][0] and current_board[0][2] != ' ':
                return current_board[0][2]
            
            return None

        for i, move in enumerate(moves):
            row, col = move[0], move[1]
            
            player_char = 'X' if i % 2 == 0 else 'O'
            board[row][col] = player_char
            
            # A winner can only be determined after at least 5 moves (3 for X, 2 for O)
            if i >= 4:
                winner_char = check_winner(board)
                if winner_char == 'X':
                    return "A"
                elif winner_char == 'O':
                    return "B"
        
        if len(moves) == 9:
            return "Draw"
        else:
            return "Pending"