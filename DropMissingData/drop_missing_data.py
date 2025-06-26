import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    """
    Removes rows with missing values in the 'name' column from the DataFrame.

    Args:
        students (pd.DataFrame): The input DataFrame with columns 'student_id', 'name', 'age'.

    Returns:
        pd.DataFrame: The DataFrame with rows having missing 'name' values removed.
    """
    df_cleaned = students.dropna(subset=['name'])
    return df_cleaned