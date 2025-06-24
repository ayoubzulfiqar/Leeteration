from datetime import datetime, timedelta

def daily_active_user_count(activity_data):
    end_date_str = "2019-07-27"
    end_date = datetime.strptime(end_date_str, "%Y-%m-%d").date()
    
    start_date = end_date - timedelta(days=29)

    daily_active_users = {}

    for record in activity_data:
        activity_date_str = record["activity_date"]
        current_activity_date = datetime.strptime(activity_date_str, "%Y-%m-%d").date()
        user_id = record["user_id"]

        if start_date <= current_activity_date <= end_date:
            if activity_date_str not in daily_active_users:
                daily_active_users[activity_date_str] = set()
            daily_active_users[activity_date_str].add(user_id)
    
    result = []
    for day_str, users_set in daily_active_users.items():
        result.append({
            "day": day_str,
            "active_users": len(users_set)
        })
    
    return result