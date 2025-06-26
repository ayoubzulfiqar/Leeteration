import datetime

def find_latest_salaries(employee_records):
    """
    Finds the latest salary for each employee from a list of salary records.

    Args:
        employee_records: A list of tuples, where each tuple is
                          (employee_id, salary, date_string).
                          date_string is expected to be in 'YYYY-MM-DD' format.

    Returns:
        A list of tuples, where each tuple is (employee_id, latest_salary),
        sorted by employee_id. If multiple records exist for the same employee
        on the same latest date, the salary from the record encountered first
        for that specific date will be retained.
    """
    latest_salaries_map = {} # Stores {employee_id: (salary, datetime.date_object)}

    for emp_id, salary, date_str in employee_records:
        current_date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()

        if emp_id not in latest_salaries_map:
            latest_salaries_map[emp_id] = (salary, current_date)
        else:
            stored_salary, stored_date = latest_salaries_map[emp_id]
            if current_date > stored_date:
                latest_salaries_map[emp_id] = (salary, current_date)
            # If current_date is equal to stored_date, the existing salary is kept.
            # If current_date is older than stored_date, no update is made.

    result = []
    for emp_id in sorted(latest_salaries_map.keys()):
        salary, _ = latest_salaries_map[emp_id]
        result.append((emp_id, salary))

    return result