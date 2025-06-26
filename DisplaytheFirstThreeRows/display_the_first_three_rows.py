import pandas as pd

def display_first_three_rows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)