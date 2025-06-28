class Solution:
    def solve(self, n: int, commands: list[str]) -> int:
        row, col = 0, 0

        for command in commands:
            if command == "UP":
                row -= 1
            elif command == "RIGHT":
                col += 1
            elif command == "DOWN":
                row += 1
            elif command == "LEFT":
                col -= 1
        
        return (row * n) + col