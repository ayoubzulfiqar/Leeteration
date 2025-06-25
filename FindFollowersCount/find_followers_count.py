```python
import pandas as pd

def find_followers_count(followers: pd.DataFrame) -> pd.DataFrame:
    """
    Calculates the number of followers for each user in the Followers table.

    Args:
        followers (pd.DataFrame): The Followers table with user_id and follower_id columns.

    Returns:
        pd.DataFrame: A table with user_id and followers_count columns, ordered by user_id.
    """
    followers_count = followers.groupby('user_id')['follower_id'].count().reset_index()
    followers_count.rename(columns={'follower_id': 'followers_count'}, inplace=True)
    followers_count = followers_count.sort_values(by='user_id')
    return followers_count
```