def project_employees_ii(employees, projects, assignments):
    """
    Finds employees who are assigned to all existing projects.

    Args:
        employees: A list of tuples, where each tuple is (employee_id, employee_name).
        projects: A list of tuples, where each tuple is (project_id, project_name).
        assignments: A list of tuples, where each tuple is (employee_id, project_id).

    Returns:
        A list of tuples, where each tuple is (employee_id, employee_name)
        for employees assigned to all projects. The results are sorted by employee_id.
    """
    
    all_project_ids = set(p_id for p_id, _ in projects)
    
    if not all_project_ids:
        return []

    employee_assigned_projects = {}
    for emp_id, proj_id in assignments:
        if emp_id not in employee_assigned_projects:
            employee_assigned_projects[emp_id] = set()
        employee_assigned_projects[emp_id].add(proj_id)

    result_employee_ids = []
    for emp_id, assigned_project_set in employee_assigned_projects.items():
        if assigned_project_set == all_project_ids:
            result_employee_ids.append(emp_id)

    employee_name_map = {emp_id: emp_name for emp_id, emp_name in employees}

    final_result = []
    result_employee_ids.sort() 
    for emp_id in result_employee_ids:
        if emp_id in employee_name_map:
            final_result.append((emp_id, employee_name_map[emp_id]))

    return final_result

if __name__ == '__main__':
    employees_data = [
        (1, 'Alice'),
        (2, 'Bob'),
        (3, 'Charlie'),
        (4, 'David')
    ]

    projects_data = [
        (101, 'Alpha Project'),
        (102, 'Beta Project'),
        (103, 'Gamma Project')
    ]

    assignments_data = [
        (1, 101),
        (1, 102),
        (1, 103),
        (2, 101),
        (2, 102),
        (3, 101),
        (4, 101),
        (4, 102),
        (4, 103)
    ]

    result1 = project_employees_ii(employees_data, projects_data, assignments_data)

    projects_data_empty = []
    assignments_data_empty_projects = [
        (1, 101),
        (1, 102)
    ]
    result2 = project_employees_ii(employees_data, projects_data_empty, assignments_data_empty_projects)

    assignments_data_empty = []
    result3 = project_employees_ii(employees_data, projects_data, assignments_data_empty)

    employees_data_with_unassigned = employees_data + [(5, 'Eve')]
    result4 = project_employees_ii(employees_data_with_unassigned, projects_data, assignments_data)