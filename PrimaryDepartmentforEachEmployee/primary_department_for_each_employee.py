```python
import pandas as pd

def primary_department(employee: pd.DataFrame) -> pd.DataFrame:
    employee['count'] = employee.groupby('employee_id')['department_id'].transform('count')
    employee_filtered = employee[((employee['primary_flag'] == 'Y') | (employee['count'] == 1))][['employee_id', 'department_id']]
    return employee_filtered
```