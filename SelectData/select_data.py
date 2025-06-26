import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    """
    Selects the name and age of the student with student_id = 101.

    Args:
        students: A pandas DataFrame with columns 'student_id', 'name', 'age'.

    Returns:
        A pandas DataFrame containing 'name' and 'age' for the student
        with student_id = 101.
    """
    selected_student = students[students['student_id'] == 101]
    result = selected_student[['name', 'age']]
    return result

if __name__ == '__main__':
    # Example 1:
    data = {
        'student_id': [101, 53, 128, 3],
        'name': ['Ulysses', 'William', 'Henry', 'Henry'],
        'age': [13, 10, 6, 11]
    }
    students_df = pd.DataFrame(data)
    output_df = selectData(students_df)
    print(output_df)

    # Example with no matching student_id
    data_no_match = {
        'student_id': [102, 53, 128, 3],
        'name': ['Alice', 'William', 'Henry', 'Henry'],
        'age': [15, 10, 6, 11]
    }
    students_df_no_match = pd.DataFrame(data_no_match)
    output_df_no_match = selectData(students_df_no_match)
    print("\nNo matching student_id:")
    print(output_df_no_match)

    # Example with multiple matching student_ids (though problem implies unique)
    # If student_id is not unique, this would return all matching rows.
    # The problem description implies student_id is a unique identifier.
    data_multiple_match = {
        'student_id': [101, 53, 128, 101],
        'name': ['Ulysses', 'William', 'Henry', 'Bob'],
        'age': [13, 10, 6, 14]
    }
    students_df_multiple_match = pd.DataFrame(data_multiple_match)
    output_df_multiple_match = selectData(students_df_multiple_match)
    print("\nMultiple matching student_ids (if applicable):")
    print(output_df_multiple_match)