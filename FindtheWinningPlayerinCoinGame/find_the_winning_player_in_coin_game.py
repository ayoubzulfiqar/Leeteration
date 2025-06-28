class Solution:
    def findWinningPlayer(self, x: int, y: int) -> str:
        max_turns_from_x = x
        max_turns_from_y = y // 4
        total_turns = min(max_turns_from_x, max_turns_from_y)
        if total_turns % 2 == 1:
            return "Alice"
        else:
            return "Bob"