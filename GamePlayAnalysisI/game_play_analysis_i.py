import pandas as pd

def game_play_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    first_login_dates = activity.groupby('player_id')['event_date'].min()
    result_df = first_login_dates.reset_index()
    result_df.rename(columns={'event_date': 'first_login'}, inplace=True)
    return result_df