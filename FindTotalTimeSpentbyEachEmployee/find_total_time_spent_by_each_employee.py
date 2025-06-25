```python
import pandas as pd

def find_total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['total_time'] = employees['out_time'] - employees['in_time']
    result = employees.groupby(['event_day', 'emp_id'])['total_time'].sum().reset_index()
    result.rename(columns={'event_day': 'day'}, inplace=True)
    return result
```