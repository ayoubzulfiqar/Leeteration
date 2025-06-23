import pandas as pd

def find_salespersons_without_red_orders(salesperson_data, company_data, orders_data):
    salesperson_df = pd.DataFrame(salesperson_data)
    company_df = pd.DataFrame(company_data)
    orders_df = pd.DataFrame(orders_data)

    red_company_id = company_df[company_df['name'] == 'RED']['com_id'].iloc[0]

    sales_ids_with_red_orders = orders_df[orders_df['com_id'] == red_company_id]['sales_id'].unique()

    all_sales_ids = salesperson_df['sales_id'].unique()

    sales_ids_without_red_orders = set(all_sales_ids) - set(sales_ids_with_red_orders)

    result_df = salesperson_df[salesperson_df['sales_id'].isin(list(sales_ids_without_red_orders))][['name']]

    return result_df

salesperson_data = [
    {'sales_id': 1, 'name': 'John', 'salary': 100000, 'commission_rate': 6, 'hire_date': '4/1/2006'},
    {'sales_id': 2, 'name': 'Amy', 'salary': 12000, 'commission_rate': 5, 'hire_date': '5/1/2010'},
    {'sales_id': 3, 'name': 'Mark', 'salary': 65000, 'commission_rate': 12, 'hire_date': '12/25/2008'},
    {'sales_id': 4, 'name': 'Pam', 'salary': 25000, 'commission_rate': 25, 'hire_date': '1/1/2005'},
    {'sales_id': 5, 'name': 'Alex', 'salary': 5000, 'commission_rate': 10, 'hire_date': '2/3/2007'}
]

company_data = [
    {'com_id': 1, 'name': 'RED', 'city': 'Boston'},
    {'com_id': 2, 'name': 'ORANGE', 'city': 'New York'},
    {'com_id': 3, 'name': 'YELLOW', 'city': 'Boston'},
    {'com_id': 4, 'name': 'GREEN', 'city': 'Austin'}
]

orders_data = [
    {'order_id': 1, 'order_date': '1/1/2014', 'com_id': 3, 'sales_id': 4, 'amount': 10000},
    {'order_id': 2, 'order_date': '2/1/2014', 'com_id': 4, 'sales_id': 5, 'amount': 5000},
    {'order_id': 3, 'order_date': '3/1/2014', 'com_id': 1, 'sales_id': 1, 'amount': 50000},
    {'order_id': 4, 'order_date': '4/1/2014', 'com_id': 1, 'sales_id': 4, 'amount': 25000}
]