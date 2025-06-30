import re

def find_valid_emails(users_table: list[dict]) -> list[dict]:
    valid_emails = []

    for user in users_table:
        email = user['email']

        if email.count('@') != 1:
            continue

        if not email.endswith('.com'):
            continue

        parts = email.split('@')
        username = parts[0]
        domain_with_com = parts[1]

        if not re.fullmatch(r'^[a-zA-Z0-9_]+$', username):
            continue

        domain = domain_with_com[:-4]

        if not re.fullmatch(r'^[a-zA-Z]+$', domain):
            continue

        valid_emails.append(user)

    valid_emails.sort(key=lambda x: x['user_id'])

    return valid_emails