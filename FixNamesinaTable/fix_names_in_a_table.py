def fix_names(users_table):
    for user in users_table:
        name = user['name']
        user['name'] = name[0].upper() + name[1:].lower()
    users_table.sort(key=lambda x: x['user_id'])
    return users_table