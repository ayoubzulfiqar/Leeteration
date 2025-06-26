import pandas as pd

def get_dataframe_size(players: pd.DataFrame) -> list[int]:
    """
    Calculates and displays the number of rows and columns of the given DataFrame.

    Args:
        players (pd.DataFrame): The input DataFrame.

    Returns:
        list[int]: An array [number of rows, number of columns].
    """
    num_rows, num_columns = players.shape
    return [num_rows, num_columns]

if __name__ == '__main__':
    # Example 1:
    data = {
        'player_id': [846, 749, 155, 583, 388, 883, 355, 247, 761, 642],
        'name': ['Mason', 'Riley', 'Bob', 'Isabella', 'Zachary', 'Ava', 'Violet', 'Thomas', 'Jack', 'Charlie'],
        'age': [21, 30, 28, 32, 24, 23, 18, 27, 33, 36],
        'position': ['Forward', 'Winger', 'Striker', 'Goalkeeper', 'Midfielder', 'Defender', 'Striker', 'Striker', 'Midfielder', 'Center-back'],
        'team': ['RealMadrid', 'Barcelona', 'ManchesterUnited', 'Liverpool', 'BayernMunich', 'Chelsea', 'Juventus', 'ParisSaint-Germain', 'ManchesterCity', 'Arsenal']
    }
    players_df = pd.DataFrame(data)

    result = get_dataframe_size(players_df)
    print(result)