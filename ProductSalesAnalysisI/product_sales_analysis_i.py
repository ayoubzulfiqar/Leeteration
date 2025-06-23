import pandas as pd

def product_sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    """
    Reports the product_name, year, and price for each sale_id in the Sales table.

    Args:
        sales (pd.DataFrame): DataFrame representing the Sales table with columns:
                              sale_id, product_id, year, quantity, price.
        product (pd.DataFrame): DataFrame representing the Product table with columns:
                                product_id, product_name.

    Returns:
        pd.DataFrame: A DataFrame with product_name, year, and price for each sale.
    """
    merged_df = pd.merge(sales, product, on='product_id', how='inner')
    result_df = merged_df[['product_name', 'year', 'price']]
    return result_df