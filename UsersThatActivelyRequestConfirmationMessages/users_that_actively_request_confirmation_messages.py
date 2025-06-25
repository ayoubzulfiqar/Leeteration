```python
def solve():
    """
    Analyzes user activity logs to identify users who actively request confirmation messages.

    This function simulates the process of analyzing user activity logs to identify users
    who consistently request confirmation messages after performing actions.  It uses a
    simplified model where user activity is represented by a list of events, and each
    event is a tuple containing the user ID and the event type.  The function identifies
    users who have a high ratio of confirmation requests to other actions.

    Returns:
        list: A list of user IDs who are considered to be actively requesting confirmation messages.
    """

    # Simulate user activity logs
    activity_logs = [
        (1, "action_a"),
        (1, "confirmation_request"),
        (2, "action_b"),
        (3, "action_c"),
        (3, "confirmation_request"),
        (1, "action_b"),
        (2, "confirmation_request"),
        (1, "confirmation_request"),
        (4, "action_a"),
        (4, "action_b"),
        (4, "confirmation_c"),
        (4, "confirmation_request"),
        (4, "confirmation_request"),
        (4, "confirmation_request"),
        (5, "action_a"),
    ]

    # Define a threshold for the confirmation request ratio
    confirmation_threshold = 0.5

    # Analyze user activity
    user_activity = {}
    for user_id, event_type in activity_logs:
        if user_id not in user_activity:
            user_activity[user_id] = {"total_actions": 0, "confirmation_requests": 0}
        user_activity[user_id]["total_actions"] += 1
        if event_type == "confirmation_request":
            user_activity[user_id]["confirmation_requests"] += 1

    # Identify users who actively request confirmation messages
    active_users = []
    for user_id, activity in user_activity.items():
        if activity["total_actions"] > 0:
            confirmation_ratio = activity["confirmation_requests"] / activity["total_actions"]
            if confirmation_ratio >= confirmation_threshold:
                active_users.append(user_id)

    return active_users


if __name__ == "__main__":
    active_users = solve()
    print(active_users)
```