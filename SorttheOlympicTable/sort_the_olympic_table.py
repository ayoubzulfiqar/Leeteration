```python
def sort_olympic_table(table):
    """
    Sorts an Olympic table (list of lists) based on the following criteria:
    1. Gold medals (descending)
    2. Silver medals (descending)
    3. Bronze medals (descending)
    4. Country name (ascending)

    Args:
        table: A list of lists, where each inner list represents a country
               and contains [country_name, gold_medals, silver_medals, bronze_medals].

    Returns:
        A new list of lists, sorted according to the criteria above.
    """
    return sorted(table, key=lambda x: (-x[1], -x[2], -x[3], x[0]))

if __name__ == '__main__':
    # Example usage:
    olympic_table = [
        ["USA", 39, 41, 33],
        ["China", 38, 32, 18],
        ["Japan", 27, 14, 17],
        ["Great Britain", 22, 21, 22],
        ["ROC", 20, 28, 23]
    ]

    sorted_table = sort_olympic_table(olympic_table)

    for country in sorted_table:
        print(country)
```
