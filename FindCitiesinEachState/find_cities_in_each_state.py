def find_cities_in_each_state(cities_data):
    """
    Groups cities by their respective states.

    Args:
        cities_data (list of tuples): A list where each tuple contains
                                      (city_name, state_name).

    Returns:
        dict: A dictionary where keys are state names and values are
              lists of city names belonging to that state.
    """
    state_cities = {}
    for city, state in cities_data:
        if state not in state_cities:
            state_cities[state] = []
        state_cities[state].append(city)
    return state_cities

if __name__ == "__main__":
    # Sample input data
    sample_cities = [
        ("New York City", "New York"),
        ("Los Angeles", "California"),
        ("Chicago", "Illinois"),
        ("San Francisco", "California"),
        ("Buffalo", "New York"),
        ("Springfield", "Illinois"),
        ("Houston", "Texas"),
        ("Austin", "Texas"),
        ("Miami", "Florida")
    ]

    # Find cities in each state
    result = find_cities_in_each_state(sample_cities)

    # Print the result (for demonstration purposes, not part of the core function)
    # This part would typically be removed if only the function is required.
    for state, cities in result.items():
        print(f"{state}: {cities}")