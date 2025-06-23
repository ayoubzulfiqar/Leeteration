import pandas as pd

def sales_analysis_iii(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    sales['sale_date'] = pd.to_datetime(sales['sale_date'])

    q1_2019_start = pd.to_datetime('2019-01-01')
    q1_2019_end = pd.to_datetime('2019-03-31')

    products_sold_outside_q1 = set(
        sales[
            (sales['sale_date'] < q1_2019_start) |
            (sales['sale_date'] > q1_2019_end)
        ]['product_id'].unique()
    )

    products_sold_in_q1 = set(
        sales[
            (sales['sale_date'] >= q1_2019_start) &
            (sales['sale_date'] <= q1_2019_end)
        ]['product_id'].unique()
    )

    eligible_product_ids = products_sold_in_q1 - products_sold_outside_q1

    result_df = product[product['product_id'].isin(list(eligible_product_ids))]

    return result_df[['product_id', 'product_name']]