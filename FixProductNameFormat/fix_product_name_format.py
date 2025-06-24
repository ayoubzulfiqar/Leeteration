def fix_product_name(product_name: str) -> str:
    """
    Normalizes and formats a product name string.

    This function performs the following operations:
    1. Strips leading and trailing whitespace.
    2. Replaces multiple internal spaces with a single space.
    3. Converts the name to title case (first letter of each word capitalized).

    Args:
        product_name: The input product name string.

    Returns:
        The formatted product name string.
    """
    if not isinstance(product_name, str):
        return ""

    # Step 1 & 2: Strip leading/trailing whitespace and normalize internal spaces.
    # split() without arguments handles all types of whitespace (spaces, tabs, newlines)
    # and treats multiple whitespace characters as a single delimiter,
    # effectively removing empty strings from the resulting list.
    cleaned_parts = product_name.strip().split()
    normalized_name = ' '.join(cleaned_parts)

    # Step 3: Convert to title case.
    # The .title() method capitalizes the first letter of each word
    # (words are typically separated by spaces, hyphens, or apostrophes).
    formatted_name = normalized_name.title()

    return formatted_name

if __name__ == '__main__':
    # Example usage (no output to console, just demonstrates functionality)
    sample_names = [
        "  apple iPhone   13 pRo  ",
        "samsung GALAXY s21 ultra",
        "  sony   PLAYSTATION   5 digital edition  ",
        "hp spectre x360 14",
        "dell xps 15",
        "  lg oled tv c1 series ",
        "bose quietcomfort 35 ii",
        "google pixel 6 pro",
        "amazon echo dot 4th gen",
        "microsoft surface laptop studio",
        "",
        "   ",
        "product-xyz-model-abc",
        "foo's bar product",
        "123 product",
        "product 123",
    ]

    fixed_names = [fix_product_name(name) for name in sample_names]

    # The fixed_names list now contains the processed strings.
    # For example:
    # fixed_names[0] would be "Apple Iphone 13 Pro"
    # fixed_names[1] would be "Samsung Galaxy S21 Ultra"
    # fixed_names[10] would be ""
    # fixed_names[11] would be ""
    # fixed_names[12] would be "Product-Xyz-Model-Abc"
    # fixed_names[13] would be "Foo'S Bar Product"
    # fixed_names[14] would be "123 Product"
    # fixed_names[15] would be "Product 123"