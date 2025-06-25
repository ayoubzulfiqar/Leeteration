```python
import pandas as pd

def solve():
    employees_data = {
        'employee_id': [2, 4, 5],
        'name': ['Crew', 'Haven', 'Kristian']
    }
    employees = pd.DataFrame(employees_data)

    salaries_data = {
        'employee_id': [5, 1, 4],
        'salary': [76071, 22517, 63539]
    }
    salaries = pd.DataFrame(salaries_data)

    merged_df = pd.merge(employees, salaries, on='employee_id', how='outer')

    missing_info = merged_df[merged_df['name'].isnull() | merged_df['salary'].isnull()]['employee_id'].sort_values()

    result_df = pd.DataFrame(missing_info)
    result_df.columns = ['employee_id']

    return result_df

if __name__ == "__main__":
    result = solve()
    print(result.to_string(index=False))
```