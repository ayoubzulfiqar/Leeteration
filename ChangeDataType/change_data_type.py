import pandas as pd

def correct_errors(students: pd.DataFrame) -> pd.DataFrame:
    """
    Corrects errors in the DataFrame by converting the 'grade' column
    from float to integer type.

    Args:
        students (pd.DataFrame): The input DataFrame with student data.

    Returns:
        pd.DataFrame: The DataFrame with the 'grade' column converted to integers.
    """
    students['grade'] = students['grade'].astype(int)
    return students

if __name__ == '__main__':
    # Example 1:
    data1 = {
        'student_id': [1, 2],
        'name': ['Ava', 'Kate'],
        'age': [6, 15],
        'grade': [73.0, 87.0]
    }
    students_df1 = pd.DataFrame(data1)
    result_df1 = correct_errors(students_df1)
    print("Example 1 Output:")
    print(result_df1)
    print("\nData types after conversion:")
    print(result_df1.dtypes)

    # Example 2: Another test case
    data2 = {
        'student_id': [3, 4, 5],
        'name': ['John', 'Emily', 'Mike'],
        'age': [10, 12, 9],
        'grade': [90.5, 78.9, 85.0]
    }
    students_df2 = pd.DataFrame(data2)
    result_df2 = correct_errors(students_df2)
    print("\nExample 2 Output:")
    print(result_df2)
    print("\nData types after conversion:")
    print(result_df2.dtypes)