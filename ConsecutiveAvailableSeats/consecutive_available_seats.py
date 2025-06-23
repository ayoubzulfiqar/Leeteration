class Solution:
    def maxConsecutiveAvailableSeats(self, seats: list[int]) -> int:
        max_consecutive = 0
        current_consecutive = 0

        for seat in seats:
            if seat == 0:  # If the seat is available
                current_consecutive += 1
            else:  # If the seat is occupied
                max_consecutive = max(max_consecutive, current_consecutive)
                current_consecutive = 0
        
        # After the loop, check one last time for any trailing sequence of available seats
        max_consecutive = max(max_consecutive, current_consecutive)
        
        return max_consecutive