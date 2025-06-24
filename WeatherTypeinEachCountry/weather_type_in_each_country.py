def get_weather_types_per_country(weather_data):
    country_weather_types = {}
    for observation in weather_data:
        country = observation.get("country")
        weather = observation.get("weather")
        if country and weather:
            if country not in country_weather_types:
                country_weather_types[country] = set()
            country_weather_types[country].add(weather)
    return country_weather_types

if __name__ == "__main__":
    sample_weather_observations = [
        {"country": "USA", "weather": "Sunny"},
        {"country": "Canada", "weather": "Snowy"},
        {"country": "USA", "weather": "Cloudy"},
        {"country": "Canada", "weather": "Cloudy"},
        {"country": "USA", "weather": "Rainy"},
        {"country": "Mexico", "weather": "Sunny"},
        {"country": "Canada", "weather": "Snowy"},
        {"country": "Mexico", "weather": "Hot"},
        {"country": "USA", "weather": "Sunny"},
        {"country": "Brazil", "weather": "Tropical"},
        {"country": "Brazil", "weather": "Rainy"},
        {"country": "Germany", "weather": "Cloudy"},
        {"country": "Germany", "weather": "Rainy"},
        {"country": "Germany", "weather": "Snowy"},
        {"country": "Australia", "weather": "Sunny"},
        {"country": "Australia", "weather": "Hot"},
        {"country": "Australia", "weather": "Dry"},
    ]

    result = get_weather_types_per_country(sample_weather_observations)

    print("Weather Types per Country:")
    for country, weather_types in sorted(result.items()):
        print(f"- {country}: {', '.join(sorted(list(weather_types)))}")