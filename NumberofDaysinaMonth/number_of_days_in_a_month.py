import sys

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def get_days_in_month(month, year):
    if not (1 <= month <= 12):
        return -1

    if month in {1, 3, 5, 7, 8, 10, 12}:
        return 31
    elif month in {4, 6, 9, 11}:
        return 30
    elif month == 2:
        return 29 if is_leap_year(year) else 28
    else:
        return -1

if __name__ == "__main__":
    try:
        month_str = sys.stdin.readline().strip()
        year_str = sys.stdin.readline().strip()

        month = int(month_str)
        year = int(year_str)

        result = get_days_in_month(month, year)
        sys.stdout.write(str(result) + "\n")
    except ValueError:
        sys.stdout.write("-1\n")
    except Exception:
        sys.stdout.write("-1\n")