def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def get_next_day(day, month, year):
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if is_leap_year(year):
        days_in_month[2] = 29

    next_day = day + 1
    next_month = month
    next_year = year

    if next_day > days_in_month[month]:
        next_day = 1
        next_month += 1
        if next_month > 12:
            next_month = 1
            next_year += 1
    
    return next_day, next_month, next_year

day_in, month_in, year_in = map(int, input().split())

next_d, next_m, next_y = get_next_day(day_in, month_in, year_in)

print(next_d, next_m, next_y)