import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather['recordDate'] = pd.to_datetime(weather['recordDate'])
    
    df_today = weather.copy()
    df_yesterday = weather.copy()
    
    df_yesterday['recordDate'] = df_yesterday['recordDate'] + pd.Timedelta(days=1)
    
    merged_df = pd.merge(
        df_today,
        df_yesterday,
        on='recordDate',
        suffixes=('_today', '_yesterday'),
        how='inner'
    )
    
    result_df = merged_df[merged_df['temperature_today'] > merged_df['temperature_yesterday']]
    
    return result_df[['id_today']].rename(columns={'id_today': 'id'})