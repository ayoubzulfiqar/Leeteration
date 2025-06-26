import pandas as pd

def reshape_data_melt(report: pd.DataFrame) -> pd.DataFrame:
    """
    Reshapes the DataFrame from wide to long format, representing sales data for
    a product in a specific quarter.

    Args:
        report (pd.DataFrame): The input DataFrame with product and quarter sales columns.

                               Example:
                               +-------------+-----------+-----------+-----------+-----------+
                               | product     | quarter_1 | quarter_2 | quarter_3 | quarter_4 |
                               +-------------+-----------+-----------+-----------+-----------+
                               | Umbrella    | 417       | 224       | 379       | 611       |
                               | SleepingBag | 800       | 936       | 93        | 875       |
                               +-------------+-----------+-----------+-----------+-----------+

    Returns:
        pd.DataFrame: The reshaped DataFrame with 'product', 'quarter', and 'sales' columns.

                      Example:
                      +-------------+-----------+-------+
                      | product     | quarter   | sales |
                      +-------------+-----------+-------+
                      | Umbrella    | quarter_1 | 417   |
                      | SleepingBag | quarter_1 | 800   |
                      | Umbrella    | quarter_2 | 224   |
                      | SleepingBag | quarter_2 | 936   |
                      | Umbrella    | quarter_3 | 379   |
                      | SleepingBag | quarter_3 | 93    |
                      | Umbrella    | quarter_4 | 611   |
                      | SleepingBag | quarter_4 | 875   |
                      +-------------+-----------+-------+
    """
    melted_df = pd.melt(report,
                        id_vars=['product'],
                        value_vars=['quarter_1', 'quarter_2', 'quarter_3', 'quarter_4'],
                        var_name='quarter',
                        value_name='sales')
    return melted_df