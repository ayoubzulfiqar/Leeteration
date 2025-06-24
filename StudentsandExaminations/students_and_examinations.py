def find_attended_exams(students, subjects, examinations):
    all_combinations = []
    for student in students:
        for subject in subjects:
            all_combinations.append({
                'student_id': student['student_id'],
                'student_name': student['student_name'],
                'subject_name': subject['subject_name']
            })

    exam_counts = {}
    for exam in examinations:
        key = (exam['student_id'], exam['subject_name'])
        exam_counts[key] = exam_counts.get(key, 0) + 1

    result = []
    for combo in all_combinations:
        student_id = combo['student_id']
        subject_name = combo['subject_name']
        
        attended_exams = exam_counts.get((student_id, subject_name), 0)
        
        result.append({
            'student_id': student_id,
            'student_name': combo['student_name'],
            'subject_name': subject_name,
            'attended_exams': attended_exams
        })

    result.sort(key=lambda x: (x['student_id'], x['subject_name']))
    
    return result

students_data = [
    {'student_id': 1, 'student_name': 'Alice'},
    {'student_id': 2, 'student_name': 'Bob'},
    {'student_id': 13, 'student_name': 'John'},
    {'student_id': 6, 'student_name': 'Alex'}
]

subjects_data = [
    {'subject_name': 'Math'},
    {'subject_name': 'Physics'},
    {'subject_name': 'Programming'}
]

examinations_data = [
    {'student_id': 1, 'subject_name': 'Math'},
    {'student_id': 1, 'subject_name': 'Physics'},
    {'student_id': 1, 'subject_name': 'Programming'},
    {'student_id': 2, 'subject_name': 'Programming'},
    {'student_id': 1, 'subject_name': 'Physics'},
    {'student_id': 1, 'subject_name': 'Math'},
    {'student_id': 13, 'subject_name': 'Math'},
    {'student_id': 13, 'subject_name': 'Programming'},
    {'student_id': 13, 'subject_name': 'Physics'},
    {'student_id': 2, 'subject_name': 'Math'},
    {'student_id': 1, 'subject_name': 'Math'}
]

# Example usage:
# output = find_attended_exams(students_data, subjects_data, examinations_data)
# for row in output:
#     print(row)