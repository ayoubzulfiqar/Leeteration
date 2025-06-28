def find_expensive_cities(cities_data, threshold):
    expensive_cities_names = []
    for city in cities_data:
        if city['cost'] > threshold:
            expensive_cities_names.append(city['name'])
    return expensive_cities_names

if __name__ == "__main__":
    sample_cities = [
        {'name': 'Paris', 'cost': 1500},
        {'name': 'London', 'cost': 1800},
        {'name': 'Rome', 'cost': 1200},
        {'name': 'Berlin', 'cost': 900},
        {'name': 'New York', 'cost': 2000},
        {'name': 'Tokyo', 'cost': 1700},
        {'name': 'Sydney', 'cost': 1650}
    ]

    cost_threshold = 1400
    expensive_results = find_expensive_cities(sample_cities, cost_threshold)
    print(expensive_results)

    cost_threshold_2 = 1850
    expensive_results_2 = find_expensive_cities(sample_cities, cost_threshold_2)
    print(expensive_results_2)

    cost_threshold_3 = 500
    expensive_results_3 = find_expensive_cities(sample_cities, cost_threshold_3)
    print(expensive_results_3)

    cost_threshold_4 = 2500
    expensive_results_4 = find_expensive_cities(sample_cities, cost_threshold_4)
    print(expensive_results_4)