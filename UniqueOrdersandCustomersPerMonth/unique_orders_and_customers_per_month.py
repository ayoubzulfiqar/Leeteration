import datetime

def analyze_orders_per_month(orders_data):
    """
    Analyzes a list of order records to count unique orders and customers per month.

    Args:
        orders_data (list of tuples): Each tuple represents an order and should be
                                      in the format (order_id, customer_id, order_date_str).
                                      order_date_str should be in 'YYYY-MM-DD' format.

    Returns:
        dict: A dictionary where keys are (year, month) tuples and values are
              dictionaries containing 'unique_orders' and 'unique_customers' counts
              for that month.
              Example: {(2023, 1): {'unique_orders': 10, 'unique_customers': 8}}
    """
    monthly_aggregation = {}

    for order_id, customer_id, order_date_str in orders_data:
        try:
            order_date = datetime.datetime.strptime(order_date_str, '%Y-%m-%d')
            year_month_key = (order_date.year, order_date.month)

            if year_month_key not in monthly_aggregation:
                monthly_aggregation[year_month_key] = {
                    'orders': set(),
                    'customers': set()
                }

            monthly_aggregation[year_month_key]['orders'].add(order_id)
            monthly_aggregation[year_month_key]['customers'].add(customer_id)
        except ValueError:
            # Handle cases where date string is not in expected format
            # For this problem, we'll just skip malformed dates.
            # In a real-world scenario, you might log this or raise an error.
            continue

    results = {}
    for year_month, data_sets in monthly_aggregation.items():
        results[year_month] = {
            'unique_orders': len(data_sets['orders']),
            'unique_customers': len(data_sets['customers'])
        }

    # Sort results by year and month for consistent output
    sorted_results = dict(sorted(results.items()))
    return sorted_results

if __name__ == '__main__':
    # Sample Order Data: (order_id, customer_id, order_date_str)
    sample_orders = [
        ('ORD001', 'CUST001', '2023-01-15'),
        ('ORD002', 'CUST002', '2023-01-20'),
        ('ORD003', 'CUST001', '2023-01-25'), # CUST001 repeats in Jan
        ('ORD004', 'CUST003', '2023-02-01'),
        ('ORD005', 'CUST001', '2023-02-10'), # CUST001 is new for Feb
        ('ORD006', 'CUST004', '2023-02-15'),
        ('ORD007', 'CUST002', '2023-03-05'),
        ('ORD008', 'CUST005', '2023-03-10'),
        ('ORD009', 'CUST001', '2023-03-15'), # CUST001 is new for Mar
        ('ORD010', 'CUST006', '2023-03-20'),
        ('ORD011', 'CUST007', '2023-04-01'),
        ('ORD012', 'CUST007', '2023-04-05'), # CUST007 repeats in Apr
        ('ORD013', 'CUST008', '2023-04-10'),
        ('ORD014', 'CUST001', '2022-12-01'), # Order from previous year
        ('ORD015', 'CUST009', '2022-12-10'),
        ('ORD016', 'CUST009', '2022-12-15'), # CUST009 repeats in Dec 2022
        ('ORD017', 'CUST010', '2023-01-01'), # New customer for Jan 2023
    ]

    monthly_summary = analyze_orders_per_month(sample_orders)

    # Print the results
    for (year, month), counts in monthly_summary.items():
        print(f"Month: {year}-{month:02d}")
        print(f"  Unique Orders: {counts['unique_orders']}")
        print(f"  Unique Customers: {counts['unique_customers']}")
        print("-" * 30)