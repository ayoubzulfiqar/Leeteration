def immediate_food_delivery_percentage(deliveries: list[list]) -> str:
    immediate_count = 0
    total_count = 0

    for delivery in deliveries:
        order_date = delivery[2]
        customer_pref_delivery_date = delivery[3]

        total_count += 1
        if order_date == customer_pref_delivery_date:
            immediate_count += 1

    if total_count == 0:
        return "0.00"
    else:
        percentage = (immediate_count / total_count) * 100
        return f"{percentage:.2f}"