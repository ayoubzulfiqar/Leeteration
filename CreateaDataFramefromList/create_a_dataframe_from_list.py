import pandas as pd

def create_dataframe(student_data: list[list[int]]) -> pd.DataFrame:
    df = pd.DataFrame(student_data, columns=['student_id', 'age'])
    return df