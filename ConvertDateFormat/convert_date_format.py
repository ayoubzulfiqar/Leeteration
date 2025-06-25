```python
def convert_date_format(date):
    """
    Converts a date from "YYYY-MM-DD" format to "MM/DD/YYYY" format.

    Args:
        date (str): The date in "YYYY-MM-DD" format.

    Returns:
        str: The date in "MM/DD/YYYY" format.
    """
    year, month, day = date.split('-')
    return f"{month}/{day}/{year}"

if __name__ == '__main__':
    date1 = "2023-10-26"
    date2 = "2024-01-01"
    date3 = "1999-12-31"

    converted_date1 = convert_date_format(date1)
    converted_date2 = convert_date_format(date2)
    converted_date3 = convert_date_format(date3)

    print(f"Original date: {date1}, Converted date: {converted_date1}")
    print(f"Original date: {date2}, Converted date: {converted_date2}")
    print(f"Original date: {date3}, Converted date: {converted_date3}")
```
