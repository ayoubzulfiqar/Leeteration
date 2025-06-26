class Solution:
    def calculate_score(self, player_pins: list[int]) -> int:
        total_score = 0
        n = len(player_pins)
        for i in range(n):
            current_pins = player_pins[i]
            
            prev_1_strike = (i - 1 >= 0 and player_pins[i - 1] == 10)
            prev_2_strike = (i - 2 >= 0 and player_pins[i - 2] == 10)
            
            if prev_1_strike or prev_2_strike:
                total_score += 2 * current_pins
            else:
                total_score += current_pins
        return total_score

    def determineTheWinner(self, player1: list[int], player2: list[int]) -> int:
        score1 = self.calculate_score(player1)
        score2 = self.calculate_score(player2)

        if score1 > score2:
            return 1
        elif score2 > score1:
            return 2
        else:
            return 0