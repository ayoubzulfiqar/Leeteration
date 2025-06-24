def reformat_department_table(department_table):
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    
    reformatted_data = {}
    
    for row in department_table:
        dept_id = row['id']
        month = row['month']
        revenue = row['revenue']
        
        if dept_id not in reformatted_data:
            reformatted_data[dept_id] = {'id': dept_id}
            for m in months:
                reformatted_data[dept_id][f"{m}_Revenue"] = None
        
        reformatted_data[dept_id][f"{month}_Revenue"] = revenue
        
    return list(reformatted_data.values())