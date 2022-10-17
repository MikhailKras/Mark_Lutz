def get_city_country(city: str, country: str, population: int = 0) -> str:
    if population:
        return f'{city.title()}, {country.title()} - {population = }'
    else:
        return f'{city.title()}, {country.title()}'
