class Solution:
    def stringShift(self, s: str, shifts: list[list[int]]) -> str:
        total_left_shift = 0
        n = len(s)

        for direction, amount in shifts:
            if direction == 0:  # Left shift
                total_left_shift += amount
            else:  # Right shift
                total_left_shift -= amount
        
        # Normalize the total_left_shift to be within [0, n-1]
        # A negative total_left_shift means an effective right shift.
        # Python's % operator handles negative numbers correctly for this purpose,
        # e.g., -1 % 5 = 4, which means a left shift of 4 is equivalent to a right shift of 1
        # on a string of length 5.
        normalized_shift = total_left_shift % n
        
        # Perform the actual shift by splitting the string and concatenating
        return s[normalized_shift:] + s[:normalized_shift]