class Solution:
    def findPoisonedDuration(self, timeSeries: list[int], duration: int) -> int:
        total_poisoned_time = 0
        n = len(timeSeries)

        if n == 0:
            return 0

        for i in range(n):
            if i == n - 1:
                # If it's the last attack, the poison always lasts for the full duration.
                total_poisoned_time += duration
            else:
                # Calculate the time difference between the current attack and the next attack.
                time_until_next_attack = timeSeries[i+1] - timeSeries[i]
                
                # The actual poisoned duration for this specific attack is the minimum of
                # the full 'duration' and the 'time_until_next_attack'.
                # This handles cases where the next attack resets the timer early.
                total_poisoned_time += min(duration, time_until_next_attack)
        
        return total_poisoned_time