class Solution:
    def dayOfYear(self, date: str) -> int:
        year = int(date[0:4])
        month = int(date[5:7])
        day = int(date[8:10])

        # Days in each month (index 0 is unused for easier 1-based month indexing)
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        # Check for leap year
        # A year is a leap year if it is divisible by 4,
        # but not by 100 unless it is also divisible by 400.
        is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

        # Adjust February days for a leap year
        if is_leap:
            days_in_month[2] = 29

        day_number = 0
        # Sum days from preceding months
        for i in range(1, month):
            day_number += days_in_month[i]

        # Add the day of the current month
        day_number += day

        return day_number