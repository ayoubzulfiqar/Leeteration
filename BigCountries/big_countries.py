import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    df_filtered = world[(world['area'] >= 3000000) | (world['population'] >= 25000000)]
    result = df_filtered[['name', 'population', 'area']]
    return result