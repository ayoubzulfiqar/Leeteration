import collections

def calculate_customer_order_frequency(orders_data):
    customer_frequency = collections.defaultdict(int)
    for order in orders_data:
        customer_id = order.get('customer_id')
        if customer_id:
            customer_frequency[customer_id] += 1
    return dict(customer_frequency)

sample_orders = [
    {'customer_id': 'C1', 'order_id': 'O101', 'date': '2023-01-05'},
    {'customer_id': 'C2', 'order_id': 'O102', 'date': '2023-01-06'},
    {'customer_id': 'C1', 'order_id': 'O103', 'date': '2023-01-07'},
    {'customer_id': 'C3', 'order_id': 'O104', 'date': '2023-01-08'},
    {'customer_id': 'C2', 'order_id': 'O105', 'date': '2023-01-09'},
    {'customer_id': 'C1', 'order_id': 'O106', 'date': '2023-01-10'},
    {'customer_id': 'C4', 'order_id': 'O107', 'date': '2023-01-11'},
    {'customer_id': 'C1', 'order_id': 'O108', 'date': '2023-01-12'},
    {'customer_id': 'C5', 'order_id': 'O109', 'date': '2023-01-13'},
    {'customer_id': 'C2', 'order_id': 'O110', 'date': '2023-01-14'},
]

frequencies = calculate_customer_order_frequency(sample_orders)
print(frequencies)