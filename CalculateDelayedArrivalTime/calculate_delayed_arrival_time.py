class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        total_time = arrivalTime + delayedTime
        return total_time % 24