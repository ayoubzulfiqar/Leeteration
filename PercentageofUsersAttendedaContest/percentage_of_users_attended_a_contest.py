import pandas as pd

def percentage_of_users_attended_contest(users: pd.DataFrame, register: pd.DataFrame) -> pd.DataFrame:
    total_users = users['user_id'].nunique()

    if total_users == 0:
        return pd.DataFrame(columns=['contest_id', 'percentage'])

    contest_participation = register.groupby('contest_id')['user_id'].nunique().reset_index()
    contest_participation.rename(columns={'user_id': 'registered_users_count'}, inplace=True)

    contest_participation['percentage'] = (contest_participation['registered_users_count'] / total_users) * 100
    contest_participation['percentage'] = contest_participation['percentage'].round(2)

    result = contest_participation.sort_values(by=['percentage', 'contest_id'], ascending=[False, True])

    return result[['contest_id', 'percentage']]