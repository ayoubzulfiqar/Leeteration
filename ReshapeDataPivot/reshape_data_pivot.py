import pandas as pd

def pivot_weather(weather: pd.DataFrame) -> pd.DataFrame:
    pivoted_df = weather.pivot(index='month', columns='city', values='temperature')
    result_df = pivoted_df.reset_index()
    return result_df