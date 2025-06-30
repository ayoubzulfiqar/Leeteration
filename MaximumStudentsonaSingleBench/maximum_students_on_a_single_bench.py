def maxStudentsOnBench(bench_length: int, student_length: int, min_spacing: int) -> int:
    if bench_length < student_length:
        return 0

    unit_for_additional_student = student_length + min_spacing
    
    additional_students = (bench_length - student_length) // unit_for_additional_student
    
    return 1 + additional_students