```python
import pandas as pd

def solve():
    data = {'employee_id': [3, 12, 13, 1, 9, 11],
            'name': ['Mila', 'Antonella', 'Emery', 'Kalel', 'Mikaela', 'Joziah'],
            'manager_id': [9, None, None, 11, None, 6],
            'salary': [60301, 31000, 67084, 21241, 50937, 28485]}
    employees = pd.DataFrame(data)

    valid_managers = employees['employee_id'].tolist()

    filtered_employees = employees[employees['salary'] < 30000]

    filtered_employees = filtered_employees[~filtered_employees['manager_id'].isin(employees['employee_id'])]

    result = filtered_employees[['employee_id']].sort_values(by='employee_id')

    return result

if __name__ == "__main__":
    result_df = solve()
    print(result_df.to_string(index=False))
```