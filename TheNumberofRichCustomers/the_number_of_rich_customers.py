```python
import pandas as pd

def count_rich_customers(customers: pd.DataFrame) -> int:
    """Counts the number of customers with at least $1,000,000 in wealth.

    Args:
        customers (pd.DataFrame): A DataFrame with a 'wealth' column representing the wealth of each customer.

    Returns:
        int: The number of rich customers.
    """
    return len(customers[customers['wealth'] >= 1000000])
```