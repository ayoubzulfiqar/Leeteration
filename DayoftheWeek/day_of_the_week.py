from datetime import date

class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        
        # Create a date object
        d = date(year, month, day)
        
        # Get the weekday index (Monday is 0 and Sunday is 6)
        weekday_index = d.weekday()
        
        # Return the corresponding day name
        return days_of_week[weekday_index]