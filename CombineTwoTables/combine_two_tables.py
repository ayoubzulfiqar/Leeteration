def combine_tables(person_table, address_table):
    result = []
    
    address_map = {addr['personId']: addr for addr in address_table}

    for person_row in person_table:
        person_id = person_row['personId']
        first_name = person_row['firstName']
        last_name = person_row['lastName']
        
        city = None
        state = None
        
        if person_id in address_map:
            matching_address = address_map[person_id]
            city = matching_address['city']
            state = matching_address['state']
            
        result.append({
            'firstName': first_name,
            'lastName': last_name,
            'city': city,
            'state': state
        })
            
    return result