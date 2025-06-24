import pandas as pd

def get_average_selling_price(prices: pd.DataFrame, units_sold: pd.DataFrame) -> pd.DataFrame:
    prices['start_date'] = pd.to_datetime(prices['start_date'])
    prices['end_date'] = pd.to_datetime(prices['end_date'])
    units_sold['purchase_date'] = pd.to_datetime(units_sold['purchase_date'])

    merged_df = pd.merge(units_sold, prices, on='product_id', how='left')

    valid_sales = merged_df[
        (merged_df['purchase_date'] >= merged_df['start_date']) &
        (merged_df['purchase_date'] <= merged_df['end_date'])
    ]

    valid_sales['total_price_per_sale'] = valid_sales['price'] * valid_sales['units']

    product_summary = valid_sales.groupby('product_id').agg(
        total_value=('total_price_per_sale', 'sum'),
        total_units=('units', 'sum')
    ).reset_index()

    product_summary['average_price'] = product_summary['total_value'] / product_summary['total_units']

    all_product_ids = prices[['product_id']].drop_duplicates()

    result = pd.merge(all_product_ids, product_summary[['product_id', 'average_price']], on='product_id', how='left')

    result['average_price'] = result['average_price'].fillna(0)

    result['average_price'] = result['average_price'].round(2)

    return result[['product_id', 'average_price']]