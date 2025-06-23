def find_duplicate_emails(person_data: list[dict]) -> list[dict]:
    email_counts = {}
    for row in person_data:
        email = row['email']
        email_counts[email] = email_counts.get(email, 0) + 1

    duplicate_emails_list = []
    for email, count in email_counts.items():
        if count > 1:
            duplicate_emails_list.append({"Email": email})
    return duplicate_emails_list

person_table_example = [
    {"id": 1, "email": "a@b.com"},
    {"id": 2, "email": "c@d.com"},
    {"id": 3, "email": "a@b.com"}
]

duplicate_emails_result = find_duplicate_emails(person_table_example)