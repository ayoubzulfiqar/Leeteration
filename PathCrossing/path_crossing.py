class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = set()
        current_x = 0
        current_y = 0
        visited.add((current_x, current_y))

        for move in path:
            if move == 'N':
                current_y += 1
            elif move == 'S':
                current_y -= 1
            elif move == 'E':
                current_x += 1
            elif move == 'W':
                current_x -= 1
            
            if (current_x, current_y) in visited:
                return True
            else:
                visited.add((current_x, current_y))
        
        return False