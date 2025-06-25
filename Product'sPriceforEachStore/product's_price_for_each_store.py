```python
def calculate_prices(products, stores, prices):
    """
    Calculates the price of each product in each store.

    Args:
        products: A list of product names.
        stores: A list of store names.
        prices: A dictionary where keys are tuples of (product, store) and values are the prices.

    Returns:
        A dictionary where keys are product names and values are dictionaries of store names to prices.
    """

    product_prices = {}
    for product in products:
        product_prices[product] = {}
        for store in stores:
            if (product, store) in prices:
                product_prices[product][store] = prices[(product, store)]
            else:
                product_prices[product][store] = None  # Or a default value like -1, depending on the requirement
    return product_prices

if __name__ == '__main__':
    products = ["Laptop", "Keyboard", "Mouse"]
    stores = ["Amazon", "Best Buy", "Walmart"]
    prices = {
        ("Laptop", "Amazon"): 1200,
        ("Laptop", "Best Buy"): 1300,
        ("Keyboard", "Amazon"): 75,
        ("Keyboard", "Best Buy"): 80,
        ("Keyboard", "Walmart"): 70,
        ("Mouse", "Amazon"): 25,
        ("Mouse", "Best Buy"): 26
    }

    product_prices = calculate_prices(products, stores, prices)
    print(product_prices)
```