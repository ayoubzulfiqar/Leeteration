def get_average_processing_time(activity_table: list[dict]) -> list[dict]:
    process_data = {}

    for row in activity_table:
        machine_id = row['machine_id']
        process_id = row['process_id']
        activity_type = row['activity_type']
        timestamp = row['timestamp']

        key = (machine_id, process_id)
        if key not in process_data:
            process_data[key] = {}
        
        process_data[key][activity_type] = timestamp

    machine_processing_times = {}

    for (machine_id, process_id), times in process_data.items():
        start_time = times['start']
        end_time = times['end']
        
        duration = end_time - start_time

        if machine_id not in machine_processing_times:
            machine_processing_times[machine_id] = []
        machine_processing_times[machine_id].append(duration)

    result = []
    for machine_id, durations in machine_processing_times.items():
        total_duration_for_machine = sum(durations)
        num_processes_on_machine = len(durations)
        
        average_time_for_machine = total_duration_for_machine / num_processes_on_machine
        
        rounded_average_time = round(average_time_for_machine, 3)
        
        result.append({
            'machine_id': machine_id,
            'processing_time': rounded_average_time
        })
    
    return result