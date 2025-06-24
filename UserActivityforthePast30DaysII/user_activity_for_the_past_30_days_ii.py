import pandas as pd

def user_activity_for_past_30_days_ii(activity: pd.DataFrame) -> pd.DataFrame:
    activity['activity_date'] = pd.to_datetime(activity['activity_date'])
    
    end_date = pd.to_datetime('2019-07-27')
    start_date = end_date - pd.Timedelta(days=29)
    
    filtered_activity = activity[
        (activity['activity_date'] >= start_date) & 
        (activity['activity_date'] <= end_date)
    ]
    
    if filtered_activity.empty:
        return pd.DataFrame({'average_users': [0.00]})
    
    distinct_users_count = filtered_activity['user_id'].nunique()
    distinct_dates_count = filtered_activity['activity_date'].nunique()
    
    average_users = distinct_users_count / distinct_dates_count
    
    return pd.DataFrame({'average_users': [round(average_users, 2)]})