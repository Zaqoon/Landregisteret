from country import Country


def read_from_file(path='areal_tabell_csv.txt') -> str:
    with open(path, 'r', encoding='utf-8') as file:
        data = file.read()
        return data


def create_dict_from_countries(data: str) -> dict:
    country_dict = {}
    data = data.split('\n')
    for country in data:
        country_data = country.split(';')
        if len(country_data) == 2:
            name = country_data[0]
            value = int(country_data[1])
            country_dict[name] = value

    return country_dict


def populate_countries(country_dict: dict) -> dict:
    result = {}
    for name, population in country_dict.items():
        result[name] = Country(name, population=population)
    
    return result


def add_area_to_countries(countries: dict, area_dict: dict) -> dict:
    for name, area in area_dict.items():
        if name in countries:
            countries[name].area = area
        else:
            print(f"{name} was not found in countries dictionary.")

    return countries


def print_countries(countries: dict):
    for country in countries.values():
        if country.area and country.population:
            print(country)
            print('---')
        else:
            print(f"{country.name} does not have area or population.")


def compare_countries(country1: Country, country2: Country) -> Country:
    return max(country1, country2, key=lambda c: c.population or 0)


def find_highest_population_density(countries: dict) -> Country:
    highest_pop = max(countries.keys(), key=lambda country: countries[country].calculate_population_density() or 0)
    return countries[highest_pop]


def find_largest_area(countries: dict) -> str:
    return max(countries.keys(), key=lambda country: countries[country].area)


if __name__ == '__main__':
    area = read_from_file('areal_tabell_csv.txt')
    population = read_from_file('befolkning_tabell_csv.txt')
    area_dict = create_dict_from_countries(area)
    population_dict = create_dict_from_countries(population)

    country_dict = populate_countries(population_dict)  # Task e)
    country_dict = add_area_to_countries(country_dict, area_dict)   # Task f)

    highest_pop = find_highest_population_density(country_dict) # Task h)
    print(f"Highest population density:\n{highest_pop}")

    c = compare_countries(     # Task d)
        country_dict['Norge'],
        country_dict['Sverige']
    )
    print(f"Country with higher population between Norway and Sweden:\n{c}")

    print_countries(country_dict)   # Task g)
