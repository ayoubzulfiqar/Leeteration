import pandas as pd

def deleteDuplicateEmails(Person: pd.DataFrame) -> None:
    min_ids_per_email = Person.groupby('email')['id'].transform('min')
    rows_to_keep_mask = (Person['id'] == min_ids_per_email)
    indices_to_drop = Person[~rows_to_keep_mask].index
    Person.drop(indices_to_drop, inplace=True)