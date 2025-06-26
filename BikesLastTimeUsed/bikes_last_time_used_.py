import datetime

def get_bikes_last_used_time(usage_records):
    last_used_times = {}
    date_format = "%Y-%m-%d %H:%M:%S"

    for record in usage_records:
        bike_id = record["bike_id"]
        timestamp_str = record["timestamp"]
        
        try:
            current_timestamp = datetime.datetime.strptime(timestamp_str, date_format)
        except ValueError:
            continue 

        if bike_id not in last_used_times or current_timestamp > last_used_times[bike_id]:
            last_used_times[bike_id] = current_timestamp
            
    return last_used_times