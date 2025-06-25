```python
import pandas as pd

def solve():
    employees_data = {
        'employee_id': [9, 6, 4, 2],
        'name': ['Hercy', 'Alice', 'Bob', 'Winston'],
        'reports_to': [None, 9, 9, None],
        'age': [43, 41, 36, 37]
    }
    employees = pd.DataFrame(employees_data)

    reports_count = employees.groupby('reports_to')['employee_id'].count().reset_index()
    reports_count.rename(columns={'employee_id': 'reports_count', 'reports_to': 'employee_id'}, inplace=True)

    average_age = employees.groupby('reports_to')['age'].mean().apply(lambda x: round(x)).reset_index()
    average_age.rename(columns={'age': 'average_age', 'reports_to': 'employee_id'}, inplace=True)

    managers = employees[employees['employee_id'].isin(reports_count['employee_id'])]
    managers = managers[['employee_id', 'name']]

    result = pd.merge(managers, reports_count, on='employee_id')
    result = pd.merge(result, average_age, on='employee_id')

    result = result.sort_values(by='employee_id')

    return result[['employee_id', 'name', 'reports_count', 'average_age']]

if __name__ == '__main__':
    result_df = solve()
    print(result_df.to_string(index=False))
```