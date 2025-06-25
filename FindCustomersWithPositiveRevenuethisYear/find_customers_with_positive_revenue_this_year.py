```python
def find_customers_with_positive_revenue(revenues):
    """
    Finds the customers with positive revenue this year.

    Args:
        revenues: A dictionary where keys are customer IDs and values are their revenue this year.

    Returns:
        A list of customer IDs with positive revenue.
    """

    positive_revenue_customers = []
    for customer_id, revenue in revenues.items():
        if revenue > 0:
            positive_revenue_customers.append(customer_id)

    return positive_revenue_customers

if __name__ == '__main__':
    revenues = {
        "customer_1": 100,
        "customer_2": -50,
        "customer_3": 0,
        "customer_4": 200,
        "customer_5": -100
    }

    positive_customers = find_customers_with_positive_revenue(revenues)
    print(positive_customers)
```
