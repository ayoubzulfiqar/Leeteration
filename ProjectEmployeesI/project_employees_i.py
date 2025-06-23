import pandas as pd

def project_employees_i(project_df: pd.DataFrame, employee_df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculates the average experience years of all employees for each project,
    rounded to 2 digits.

    Args:
        project_df (pd.DataFrame): DataFrame representing the Project table with columns:
                                   'project_id', 'employee_id'.
        employee_df (pd.DataFrame): DataFrame representing the Employee table with columns:
                                    'employee_id', 'name', 'experience_years'.

    Returns:
        pd.DataFrame: A DataFrame with 'project_id' and 'average_years' columns,
                      representing the average experience years for each project,
                      rounded to 2 decimal places.
    """
    
    merged_df = pd.merge(project_df, employee_df, on='employee_id', how='inner')
    
    # Group by project_id and calculate the average experience_years
    average_years_df = merged_df.groupby('project_id')['experience_years'].mean().reset_index()
    
    # Round the average to 2 decimal places
    average_years_df['experience_years'] = average_years_df['experience_years'].round(2)
    
    # Rename the column as per the output format
    average_years_df = average_years_df.rename(columns={'experience_years': 'average_years'})
    
    return average_years_df

if __name__ == '__main__':
    # Example Usage:
    # Create Project DataFrame
    project_data = {
        'project_id': [1, 1, 1, 2, 2],
        'employee_id': [1, 2, 3, 1, 4]
    }
    project_df = pd.DataFrame(project_data)

    # Create Employee DataFrame
    employee_data = {
        'employee_id': [1, 2, 3, 4],
        'name': ['Khaled', 'Ali', 'John', 'Doe'],
        'experience_years': [3, 2, 1, 2]
    }
    employee_df = pd.DataFrame(employee_data)

    # Get the result
    result_df = project_employees_i(project_df, employee_df)
    print(result_df)

    # Expected Output:
    #    project_id  average_years
    # 0           1           2.00
    # 1           2           2.50