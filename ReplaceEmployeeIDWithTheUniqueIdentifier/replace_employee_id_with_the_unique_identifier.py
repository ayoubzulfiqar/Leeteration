import pandas as pd

def replace_employee_id(employees_table, employeeuni_table):
    employees_df = pd.DataFrame(employees_table)
    employeeuni_df = pd.DataFrame(employeeuni_table)

    merged_df = pd.merge(employees_df, employeeuni_df, on='id', how='left')

    result_df = merged_df[['unique_id', 'name']]

    result_df['unique_id'] = result_df['unique_id'].apply(lambda x: None if pd.isna(x) else int(x))

    return result_df