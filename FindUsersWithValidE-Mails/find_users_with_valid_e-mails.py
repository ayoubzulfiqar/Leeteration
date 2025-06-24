import re

def find_users_with_valid_emails(users_table: list[dict]) -> list[dict]:
    valid_users = []
    email_pattern = re.compile(r"^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode\.com$")

    for user in users_table:
        mail = user.get('mail', '')
        if email_pattern.match(mail):
            valid_users.append(user)
    return valid_users