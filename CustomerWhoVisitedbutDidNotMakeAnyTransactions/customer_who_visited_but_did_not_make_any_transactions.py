import pandas as pd

def find_customers_no_transactions(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    """
    Finds the IDs of customers who visited without making any transactions
    and the number of times they made these types of visits.

    Args:
        visits (pd.DataFrame): DataFrame with 'visit_id' and 'customer_id'.
        transactions (pd.DataFrame): DataFrame with 'transaction_id', 'visit_id', and 'amount'.

    Returns:
        pd.DataFrame: A DataFrame with 'customer_id' and 'count_no_trans',
                      representing customers who visited without transactions
                      and the count of such visits.
    """
    # Get all visit_ids that have corresponding transactions
    visit_ids_with_transactions = transactions['visit_id'].unique()

    # Filter the visits DataFrame to include only visits where no transaction occurred
    visits_without_transactions = visits[~visits['visit_id'].isin(visit_ids_with_transactions)]

    # Group by customer_id and count the number of visits without transactions
    # .size() returns a Series with the counts, .reset_index(name='count_no_trans')
    # converts it back to a DataFrame and names the count column.
    result = visits_without_transactions.groupby('customer_id').size().reset_index(name='count_no_trans')

    return result