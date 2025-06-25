```python
import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    """Rearranges the Products table to have (product_id, store, price) format."""

    # Melt the DataFrame to unpivot the store columns
    melted_df = pd.melt(
        products,
        id_vars=['product_id'],
        value_vars=['store1', 'store2', 'store3'],
        var_name='store',
        value_name='price'
    )

    # Drop rows where the price is null
    melted_df = melted_df.dropna(subset=['price'])

    return melted_df
```