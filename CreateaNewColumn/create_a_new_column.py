import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees['salary'] * 2
    return employees

if __name__ == '__main__':
    # Example 1 Input
    data = {'name': ['Piper', 'Grace', 'Georgia', 'Willow', 'Finn', 'Thomas'],
            'salary': [4548, 28150, 1103, 6593, 74576, 24433]}
    employees_df = pd.DataFrame(data)

    # Call the function
    result_df = createBonusColumn(employees_df)

    # Print the output
    print(result_df)