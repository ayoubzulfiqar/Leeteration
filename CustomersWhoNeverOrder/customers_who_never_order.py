def find_customers_who_never_order(customers: list[dict], orders: list[dict]) -> list[dict]:
    ordered_customer_ids = set()
    for order in orders:
        ordered_customer_ids.add(order["customerId"])

    result = []
    for customer in customers:
        if customer["id"] not in ordered_customer_ids:
            result.append({"Customers": customer["name"]})

    return result