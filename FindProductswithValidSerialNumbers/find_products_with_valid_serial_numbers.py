import re

def find_products_with_valid_serial_numbers(products: list[dict]) -> list[dict]:
    """
    Finds all products whose description contains a valid serial number pattern.

    A valid serial number follows these rules:
    - It starts with the letters SN (case-sensitive).
    - Followed by exactly 4 digits.
    - It must have a hyphen (-) followed by exactly 4 digits.

    Args:
        products: A list of dictionaries, where each dictionary represents a product
                  with keys 'product_id', 'product_name', and 'description'.

    Returns:
        A list of dictionaries representing the products with valid serial numbers,
        ordered by product_id in ascending order.
    """
    valid_products = []
    # Regular expression for a valid serial number: SN + 4 digits + - + 4 digits
    # \d matches any digit (0-9)
    # {4} matches the preceding token exactly 4 times
    serial_pattern = re.compile(r"SN\d{4}-\d{4}")

    for product in products:
        description = product.get('description', '')
        if serial_pattern.search(description):
            valid_products.append(product)

    # Sort the result by product_id in ascending order
    valid_products.sort(key=lambda x: x['product_id'])

    return valid_products