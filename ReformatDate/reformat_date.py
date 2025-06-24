class Solution:
    def reformatDate(self, date: str) -> str:
        month_map = {
            "Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04",
            "May": "05", "Jun": "06", "Jul": "07", "Aug": "08",
            "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"
        }

        parts = date.split()
        
        day_str = parts[0]
        month_abbr = parts[1]
        year_str = parts[2]

        # Process Day
        # Remove the "st", "nd", "rd", "th" suffix
        # The day number is always at least one digit, so day_str[:-2] is safe
        day_num = day_str[:-2]
        formatted_day = f"{int(day_num):02d}"

        # Process Month
        formatted_month = month_map[month_abbr]

        # Year is already in YYYY format
        formatted_year = year_str

        return f"{formatted_year}-{formatted_month}-{formatted_day}"