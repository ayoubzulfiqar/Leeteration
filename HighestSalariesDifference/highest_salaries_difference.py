def highest_salaries_difference(salaries: list) -> float:
    """
    Calculates the difference between the highest and lowest salaries in a list.

    Args:
        salaries: A list of numerical salaries (int or float).

    Returns:
        The difference between the maximum and minimum salary.
        Returns 0.0 if the list is empty or contains only one element.
    """
    if not salaries:
        return 0.0
    
    if len(salaries) == 1:
        return 0.0

    max_salary = salaries[0]
    min_salary = salaries[0]

    for salary in salaries:
        if salary > max_salary:
            max_salary = salary
        if salary < min_salary:
            min_salary = salary
            
    return float(max_salary - min_salary)

# Example usage (not part of the strict output, for testing purposes only)
# if __name__ == "__main__":
#     print(highest_salaries_difference([1000, 5000, 2000, 8000]))  # Expected: 7000.0
#     print(highest_salaries_difference([100.5, 200.75, 50.25]))   # Expected: 150.5
#     print(highest_salaries_difference([5000]))                   # Expected: 0.0
#     print(highest_salaries_difference([]))                       # Expected: 0.0
#     print(highest_salaries_difference([7000, 7000, 7000]))       # Expected: 0.0
#     print(highest_salaries_difference([-100, -500, -200]))      # Expected: 400.0 (max - min = -100 - (-500) = 400)
