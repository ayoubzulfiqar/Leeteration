def find_students_with_invalid_departments(students_data, departments_data):
    """
    Finds students whose department ID does not exist in the departments data.

    Args:
        students_data (list of dict): A list of dictionaries, where each dictionary
                                      represents a student with keys like 'student_id',
                                      'student_name', and 'dept_id'.
        departments_data (list of dict): A list of dictionaries, where each dictionary
                                         represents a department with keys like 'dept_id'
                                         and 'dept_name'.

    Returns:
        list of dict: A list of dictionaries, each containing 'student_id' and
                      'student_name' for students with invalid department IDs.
    """
    valid_dept_ids = set()
    for dept in departments_data:
        valid_dept_ids.add(dept['dept_id'])

    result = []
    for student in students_data:
        # Check if 'dept_id' key exists and its value is not in valid_dept_ids
        # or if 'dept_id' key is missing/None (assuming None/missing is invalid)
        if 'dept_id' not in student or student['dept_id'] not in valid_dept_ids:
            result.append({
                'student_id': student['student_id'],
                'student_name': student['student_name']
            })
    return result

if __name__ == "__main__":
    # Example Usage:
    students_table = [
        {'student_id': 1, 'student_name': 'Alice', 'dept_id': 101},
        {'student_id': 2, 'student_name': 'Bob', 'dept_id': 102},
        {'student_id': 3, 'student_name': 'Charlie', 'dept_id': 103}, # Invalid dept_id
        {'student_id': 4, 'student_name': 'David', 'dept_id': None},  # Invalid dept_id (None)
        {'student_id': 5, 'student_name': 'Eve', 'dept_id': 101},
        {'student_id': 6, 'student_name': 'Frank', 'dept_id': 104}   # Invalid dept_id
    ]

    departments_table = [
        {'dept_id': 101, 'dept_name': 'Computer Science'},
        {'dept_id': 102, 'dept_name': 'Mathematics'},
        {'dept_id': 105, 'dept_name': 'Physics'}
    ]

    invalid_students = find_students_with_invalid_departments(students_table, departments_table)
    print(invalid_students)

    # Another example: All students have valid departments
    students_table_2 = [
        {'student_id': 10, 'student_name': 'Grace', 'dept_id': 101},
        {'student_id': 11, 'student_name': 'Heidi', 'dept_id': 102}
    ]
    departments_table_2 = [
        {'dept_id': 101, 'dept_name': 'Art'},
        {'dept_id': 102, 'dept_name': 'Music'}
    ]
    invalid_students_2 = find_students_with_invalid_departments(students_table_2, departments_table_2)
    print(invalid_students_2)

    # Example: Empty students table
    students_table_3 = []
    departments_table_3 = [
        {'dept_id': 101, 'dept_name': 'History'}
    ]
    invalid_students_3 = find_students_with_invalid_departments(students_table_3, departments_table_3)
    print(invalid_students_3)

    # Example: Empty departments table (all students will be invalid)
    students_table_4 = [
        {'student_id': 20, 'student_name': 'Ivy', 'dept_id': 201},
        {'student_id': 21, 'student_name': 'Jack', 'dept_id': 202}
    ]
    departments_table_4 = []
    invalid_students_4 = find_students_with_invalid_departments(students_table_4, departments_table_4)
    print(invalid_students_4)