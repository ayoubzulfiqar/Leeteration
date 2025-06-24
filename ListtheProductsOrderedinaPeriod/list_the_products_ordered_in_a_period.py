import pandas as pd

def list_products_ordered_in_period(products: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    orders['order_date'] = pd.to_datetime(orders['order_date'])
    
    feb_2020_orders = orders[
        (orders['order_date'].dt.year == 2020) & 
        (orders['order_date'].dt.month == 2)
    ]
    
    product_units_feb_2020 = feb_2020_orders.groupby('product_id')['unit'].sum().reset_index()
    
    high_volume_products = product_units_feb_2020[product_units_feb_2020['unit'] >= 100]
    
    result = pd.merge(
        high_volume_products,
        products,
        on='product_id',
        how='inner'
    )
    
    return result[['product_name', 'unit']]