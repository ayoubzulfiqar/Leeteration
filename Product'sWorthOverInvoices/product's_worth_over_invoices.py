def calculate_products_worth_over_invoices(products_data, invoices_data):
    total_product_worth = 0.0
    for product in products_data:
        total_product_worth += product['price'] * product['quantity']

    total_invoice_amount = sum(invoices_data)

    return total_product_worth - total_invoice_amount

if __name__ == '__main__':
    products_example_1 = [
        {'price': 1200.0, 'quantity': 2},
        {'price': 25.0, 'quantity': 10},
        {'price': 75.0, 'quantity': 5}
    ]
    invoices_example_1 = [2000.0, 500.0, 100.0]
    
    result_1 = calculate_products_worth_over_invoices(products_example_1, invoices_example_1)
    print(result_1)

    products_example_2 = [
        {'price': 300.0, 'quantity': 3}
    ]
    invoices_example_2 = [1000.0]

    result_2 = calculate_products_worth_over_invoices(products_example_2, invoices_example_2)
    print(result_2)

    products_example_3 = []
    invoices_example_3 = [50.0, 20.0]

    result_3 = calculate_products_worth_over_invoices(products_example_3, invoices_example_3)
    print(result_3)

    products_example_4 = [
        {'price': 20.0, 'quantity': 5}
    ]
    invoices_example_4 = []

    result_4 = calculate_products_worth_over_invoices(products_example_4, invoices_example_4)
    print(result_4)