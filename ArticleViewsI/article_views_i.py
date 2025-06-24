import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    filtered_views = views[views['author_id'] == views['viewer_id']]
    unique_authors = sorted(filtered_views['author_id'].unique())
    result_df = pd.DataFrame({'id': unique_authors})
    return result_df