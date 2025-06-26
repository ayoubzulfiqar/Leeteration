import pandas as pd

def fillMissingData(products: pd.DataFrame) -> pd.DataFrame:
    products['quantity'] = products['quantity'].fillna(0)
    return products

if __name__ == '__main__':
    # Example 1:
    data1 = {
        'name': ['Wristwatch', 'WirelessEarbuds', 'GolfClubs', 'Printer'],
        'quantity': [None, None, 779, 849],
        'price': [135, 821, 9319, 3051]
    }
    products_df1 = pd.DataFrame(data1)
    result_df1 = fillMissingData(products_df1)
    print("Example 1 Output:")
    print(result_df1)

    # Example 2: No missing values
    data2 = {
        'name': ['Laptop', 'Mouse', 'Keyboard'],
        'quantity': [100, 250, 150],
        'price': [1200, 25, 75]
    }
    products_df2 = pd.DataFrame(data2)
    result_df2 = fillMissingData(products_df2)
    print("\nExample 2 Output (no missing values):")
    print(result_df2)

    # Example 3: All missing values
    data3 = {
        'name': ['Monitor', 'Webcam'],
        'quantity': [None, None],
        'price': [300, 50]
    }
    products_df3 = pd.DataFrame(data3)
    result_df3 = fillMissingData(products_df3)
    print("\nExample 3 Output (all missing values):")
    print(result_df3)