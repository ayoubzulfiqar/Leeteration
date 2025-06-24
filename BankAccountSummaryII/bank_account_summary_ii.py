import pandas as pd

def bank_account_summary(users: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    account_balances = transactions.groupby('account')['amount'].sum().reset_index()
    account_balances.rename(columns={'amount': 'balance'}, inplace=True)
    
    merged_df = pd.merge(users, account_balances, on='account', how='left')
    
    merged_df['balance'] = merged_df['balance'].fillna(0)
    
    result_df = merged_df[merged_df['balance'] > 10000]
    
    return result_df[['name', 'balance']]