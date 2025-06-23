import pandas as pd

def find_employees_earning_more_than_managers(employee_df: pd.DataFrame) -> pd.DataFrame:
    merged_df = employee_df.merge(
        employee_df,
        left_on='managerId',
        right_on='id',
        how='inner',
        suffixes=('_employee', '_manager')
    )
    
    result_df = merged_df[merged_df['salary_employee'] > merged_df['salary_manager']]
    
    final_output = result_df[['name_employee']].rename(columns={'name_employee': 'Employee'})
    
    return final_output

data = {
    'id': [1, 2, 3, 4],
    'name': ['Joe', 'Henry', 'Sam', 'Max'],
    'salary': [70000, 80000, 60000, 90000],
    'managerId': [3, 4, None, None]
}
employee_df = pd.DataFrame(data)

output_df = find_employees_earning_more_than_managers(employee_df)