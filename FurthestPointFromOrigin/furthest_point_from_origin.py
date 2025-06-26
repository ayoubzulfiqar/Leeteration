class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        l_count = 0
        r_count = 0
        u_count = 0

        for move in moves:
            if move == 'L':
                l_count += 1
            elif move == 'R':
                r_count += 1
            else: # move == '_'
                u_count += 1

        # Calculate the maximum possible position by treating all '_' as 'R'
        # The position is (number of R moves) - (number of L moves)
        max_position = r_count - l_count + u_count

        # Calculate the minimum possible position by treating all '_' as 'L'
        min_position = r_count - l_count - u_count
        
        # The furthest distance from the origin is the maximum of the absolute
        # values of these two extreme reachable positions.
        return max(abs(max_position), abs(min_position))