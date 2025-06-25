```python
def longestTask(n, logs):
    max_time = 0
    employee_id = -1
    start_time = 0
    for log in logs:
        emp_id = log[0]
        leave_time = log[1]
        task_time = leave_time - start_time
        if task_time > max_time:
            max_time = task_time
            employee_id = emp_id
        elif task_time == max_time:
            employee_id = min(employee_id, emp_id)
        start_time = leave_time
    return employee_id
```