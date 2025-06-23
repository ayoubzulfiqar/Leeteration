def analyze_sales(sales_data):
    total_revenue = 0.0
    revenue_by_product = {}

    for sale in sales_data:
        product_name = sale.get('product_name')
        sale_amount = sale.get('sale_amount')

        if product_name is None or sale_amount is None:
            continue

        total_revenue += sale_amount

        if product_name in revenue_by_product:
            revenue_by_product[product_name] += sale_amount
        else:
            revenue_by_product[product_name] = sale_amount

    sorted_revenue_by_product = dict(sorted(revenue_by_product.items(), key=lambda item: item[1], reverse=True))

    analysis_results = {
        'total_revenue': total_revenue,
        'revenue_by_product': sorted_revenue_by_product
    }
    return analysis_results