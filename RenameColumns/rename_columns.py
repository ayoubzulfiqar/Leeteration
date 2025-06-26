import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    """
    Renames columns in the DataFrame as follows:
    id to student_id
    first to first_name
    last to last_name
    age to age_in_years

    Args:
        students (pd.DataFrame): The input DataFrame with columns 'id', 'first', 'last', 'age'.

    Returns:
        pd.DataFrame: The DataFrame with renamed columns.
    """
    return students.rename(columns={
        'id': 'student_id',
        'first': 'first_name',
        'last': 'last_name',
        'age': 'age_in_years'
    })