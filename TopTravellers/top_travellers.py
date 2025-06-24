import pandas as pd

def top_travellers(users: pd.DataFrame, rides: pd.DataFrame) -> pd.DataFrame:
    """
    Calculates the total distance traveled by each user and returns the result
    ordered by travelled_distance in descending order, then by name in ascending order.

    Args:
        users (pd.DataFrame): DataFrame with 'id' and 'name' columns.
        rides (pd.DataFrame): DataFrame with 'id', 'user_id', and 'distance' columns.

    Returns:
        pd.DataFrame: A DataFrame with 'name' and 'travelled_distance' columns.
    """
    
    # Calculate total distance for each user from the rides table
    # Group by user_id and sum the distance
    user_distances = rides.groupby('user_id')['distance'].sum().reset_index()
    user_distances.rename(columns={'distance': 'travelled_distance'}, inplace=True)
    
    # Merge with the users table to get user names and include users with no rides
    # Use a left merge to keep all users from the 'users' table
    result_df = pd.merge(users, user_distances, left_on='id', right_on='user_id', how='left')
    
    # Fill NaN values for users who had no rides with 0
    result_df['travelled_distance'].fillna(0, inplace=True)
    
    # Convert 'travelled_distance' to integer type as distances are integers
    result_df['travelled_distance'] = result_df['travelled_distance'].astype(int)
    
    # Select only the required columns: name and travelled_distance
    result_df = result_df[['name', 'travelled_distance']]
    
    # Sort the results:
    # 1. By travelled_distance in descending order
    # 2. Then by name in ascending order (for ties in distance)
    result_df = result_df.sort_values(by=['travelled_distance', 'name'], ascending=[False, True])
    
    return result_df