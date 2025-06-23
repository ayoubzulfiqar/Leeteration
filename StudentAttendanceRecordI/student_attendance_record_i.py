class Solution:
    def checkRecord(self, s: str) -> bool:
        absent_count = 0
        late_consecutive_count = 0

        for char in s:
            if char == 'A':
                absent_count += 1
                late_consecutive_count = 0  # Reset consecutive 'L's if 'A' or 'P' is encountered
                if absent_count >= 2:
                    return False
            elif char == 'L':
                late_consecutive_count += 1
                if late_consecutive_count >= 3:
                    return False
            else:  # char == 'P'
                late_consecutive_count = 0  # Reset consecutive 'L's

        return True