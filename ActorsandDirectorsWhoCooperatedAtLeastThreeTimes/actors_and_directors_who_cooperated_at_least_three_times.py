import pandas as pd

def find_cooperating_pairs(actor_director: pd.DataFrame) -> pd.DataFrame:
    cooperation_counts = actor_director.groupby(['actor_id', 'director_id']).size().reset_index(name='cooperation_count')
    
    result = cooperation_counts[cooperation_counts['cooperation_count'] >= 3]
    
    return result[['actor_id', 'director_id']]