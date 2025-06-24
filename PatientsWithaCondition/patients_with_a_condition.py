def findPatientsWithDiabetes(patients: list[dict]) -> list[dict]:
    result = []
    for patient in patients:
        conditions_str = patient["conditions"]
        
        # Split the conditions string into individual codes.
        # filter(None, ...) removes any empty strings that might result from multiple spaces
        # or an empty conditions string.
        codes = list(filter(None, conditions_str.split(' ')))
        
        found_diabetes = False
        for code in codes:
            if code.startswith('DIAB1'):
                found_diabetes = True
                break 
        
        if found_diabetes:
            result.append(patient)
            
    return result