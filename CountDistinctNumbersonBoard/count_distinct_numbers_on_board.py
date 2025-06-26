import collections

class Solution:
    def distinctNumbersOnBoard(self, n: int) -> int:
        board = set()
        q = collections.deque()

        board.add(n)
        q.append(n)

        while q:
            x = q.popleft()

            for i in range(2, n + 1):
                if x % i == 1:
                    if i not in board:
                        board.add(i)
                        q.append(i)
        
        return len(board)