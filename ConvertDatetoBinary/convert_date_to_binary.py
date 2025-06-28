def date_to_binary(date: str) -> str:
    parts = date.split('-')
    year_str = parts[0]
    month_str = parts[1]
    day_str = parts[2]

    year_int = int(year_str)
    month_int = int(month_str)
    day_int = int(day_str)

    year_bin = bin(year_int)[2:]
    month_bin = bin(month_int)[2:]
    day_bin = bin(day_int)[2:]

    return f"{year_bin}-{month_bin}-{day_bin}"

if __name__ == '__main__':
    # Example 1
    date1 = "2080-02-29"
    result1 = date_to_binary(date1)
    print(result1)

    # Example 2
    date2 = "1900-01-01"
    result2 = date_to_binary(date2)
    print(result2)