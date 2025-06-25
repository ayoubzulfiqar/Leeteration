```python
import pandas as pd

def latest_login(logins: pd.DataFrame) -> pd.DataFrame:
    logins['year'] = pd.to_datetime(logins['time_stamp']).dt.year
    logins_2020 = logins[logins['year'] == 2020]
    
    if logins_2020.empty:
        return pd.DataFrame(columns=['user_id', 'last_stamp'])
    
    latest_logins = logins_2020.groupby('user_id')['time_stamp'].max().reset_index()
    latest_logins.rename(columns={'time_stamp': 'last_stamp'}, inplace=True)
    return latest_logins
```