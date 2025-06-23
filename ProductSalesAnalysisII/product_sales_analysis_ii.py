def product_sales_analysis_ii(sales_data):
    product_summary = {}

    for sale in sales_data:
        product_id = sale['product_id']
        quantity = sale['quantity']
        price = sale['price']

        if product_id not in product_summary:
            product_summary[product_id] = {
                'total_quantity': 0,
                'total_price': 0
            }
        
        product_summary[product_id]['total_quantity'] += quantity
        product_summary[product_id]['total_price'] += price
    
    result = []
    for product_id, totals in product_summary.items():
        result.append({
            'product_id': product_id,
            'total_quantity': totals['total_quantity'],
            'total_price': totals['total_price']
        })
    
    return result