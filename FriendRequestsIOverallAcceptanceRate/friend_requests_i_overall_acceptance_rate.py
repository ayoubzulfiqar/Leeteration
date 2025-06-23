def calculate_friend_request_acceptance_rate(requests):
    if not requests:
        return 0.0
    
    total_requests = len(requests)
    accepted_requests = 0
    
    for request in requests:
        # Assuming each request is a sequence (e.g., tuple or list)
        # where the third element (index 2) indicates acceptance status (True for accepted, False for rejected)
        if request[2]:
            accepted_requests += 1
            
    return float(accepted_requests) / total_requests