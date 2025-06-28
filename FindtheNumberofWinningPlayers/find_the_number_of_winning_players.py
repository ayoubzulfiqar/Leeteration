import collections

class Solution:
    def findWinningPlayers(self, n: int, pick: list[list[int]]) -> int:
        player_balls_counts = collections.defaultdict(lambda: collections.defaultdict(int))

        for player_id, color_id in pick:
            player_balls_counts[player_id][color_id] += 1

        winning_players_count = 0

        for i in range(n):
            max_same_color_count = 0
            if i in player_balls_counts:
                max_same_color_count = max(player_balls_counts[i].values())
            
            if max_same_color_count >= (i + 1):
                winning_players_count += 1
                
        return winning_players_count