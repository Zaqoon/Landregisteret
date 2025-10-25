# Øvingsoppgave 9 i DAT120

This project reads population and area data for countries, creates `Country` objects, and compares them.

## Files

### `country.py`
Defines the `Country` class with:
- **Attributes:** `name`, `population`, `area`, and `population_density`
- **Methods:**
  - `__init__()`: sets basic info
  - `__str__()`: prints readable country info
  - `calculate_population_density()`: computes people per square km

### Main Script
Handles data loading, object creation, and analysis.

#### Functions
- **`read_from_file(path)`** — Reads file contents as text.  
- **`create_dict_from_countries(data)`** — Converts text data into a `{country: value}` dictionary.  
- **`populate_countries(country_dict)`** — Creates `Country` objects from population data.  
- **`add_area_to_countries(countries, area_dict)`** — Adds area info to each country.  
- **`print_countries(countries)`** — Prints all countries with details.  
- **`compare_countries(country1, country2)`** — Returns the country with a larger population.  
- **`find_highest_population_density(countries)`** — Finds the most crowded country.  
- **`find_largest_area(countries)`** — Finds the country with the biggest area.

### Main Program
1. Reads population and area files.  
2. Builds dictionaries and `Country` objects.  
3. Adds area info to countries.  
4. Finds the country with:
   - Highest population density  
   - Largest area  
   - Greater population between Norway and Sweden  
5. Prints results.

---

This is a simple example of reading data, creating objects, and performing calculations.

---

## Key logic explained

This section goes deeper into the trickier parts of the code: how we build `Country` objects, how we calculate density, and how we pick "the biggest" country based on some rule.

### 1. Turning file text into dictionaries

We start with text files that look like this:

```text
Norge;5400000
Sverige;10500000
Danmark;5920000
```

Each line is `land;verdi`.

We convert that into a dictionary with `create_dict_from_countries`:

```python
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
```

**What it does:**
- `data.split('\n')` splits the big string into lines.
- Each line is split on `;` to get `[name, number]`.
- We convert the number to `int` and store it in a dictionary.

**Result example:**
```python
{
    "Norge": 5400000,
    "Sverige": 10500000,
    "Danmark": 5920000
}
```

We use this both for population and for area.

---

### 2. Building `Country` objects from those dictionaries

Once we have the population dictionary, we turn each entry into a `Country` object using `populate_countries`:

```python
def populate_countries(country_dict: dict) -> dict:
    result = {}
    for name, population in country_dict.items():
        result[name] = Country(name, population=population)
    return result
```

**What it does:**
- Loops through each `name, population` pair.
- Creates a `Country` with that data.
- Stores all the `Country` objects in a new dictionary so we can access them by name later.

Then we add area using `add_area_to_countries`:

```python
def add_area_to_countries(countries: dict, area_dict: dict) -> dict:
    for name, area in area_dict.items():
        if name in countries:
            countries[name].area = area
        else:
            print(f"{name} was not found in countries dictionary.")
    return countries
```

Now each `Country` object has both `population` AND `area`.

---

### 3. The `Country` class and population density

```python
class Country:
    def __init__(self, name, population=0, area=0):
        self.name = name
        self.population = population
        self.area = area

    def calculate_population_density(self):
        if self.area and self.population:
            self.population_density = round(self.population / self.area, 2)
        else:
            self.population_density = None
        return self.population_density

    def __str__(self):
        self.calculate_population_density()
        if self.population_density is not None:
            return (
                f"Name: {self.name}\n"
                f"Population: {self.population}\n"
                f"Area: {self.area}\n"
                f"Population Density: {self.population_density}"
            )
        else:
            return (
                f"Name: {self.name}\n"
                f"Population: {self.population}\n"
                f"Area: {self.area}"
            )
```

**Key ideas:**
- `calculate_population_density()` computes `population / area` and rounds to 2 decimals.
- If data is missing, it sets `population_density = None`.
- `__str__()` is called when you `print(country)`, and it automatically calculates density before showing the info.

Example output:

```
Name: Norge
Population: 5400000
Area: 385207
Population Density: 14.02
```

---

### 4. Finding the country with highest population density

```python
def find_highest_population_density(countries: dict) -> Country:
    highest_pop = max(
        countries.keys(),
        key=lambda country: countries[country].calculate_population_density() or 0
    )
    return countries[highest_pop]
```

**What happens:**
- Loops through all countries.
- Calculates density for each one.
- Returns the country with the highest density.
- Uses `or 0` to handle cases where density might be `None`.

---

### 5. Comparing two countries by population

```python
def compare_countries(country1: Country, country2: Country) -> Country:
    return max(country1, country2, key=lambda c: c.population or 0)
```

**Explanation:**
- Uses Python’s `max()` with a custom key to pick the country with the higher population.
- `or 0` ensures no crash if population is missing.

Example:
```python
bigger = compare_countries(country_dict['Norge'], country_dict['Sverige'])
print(bigger)
```

---

### 6. The `if __name__ == '__main__':` block

This is the main program that runs when you execute the file directly:

```python
if __name__ == '__main__':
    area = read_from_file('areal_tabell_csv.txt')
    population = read_from_file('befolkning_tabell_csv.txt')
    area_dict = create_dict_from_countries(area)
    population_dict = create_dict_from_countries(population)

    country_dict = populate_countries(population_dict)
    country_dict = add_area_to_countries(country_dict, area_dict)

    highest_pop = find_highest_population_density(country_dict)
    print(f"Highest population density:\n{highest_pop}")

    c = compare_countries(country_dict['Norge'], country_dict['Sverige'])
    print(f"Country with higher population between Norway and Sweden:\n{c}")

    print_countries(country_dict)
```

**Purpose:**
- Reads the two data files.
- Builds and enriches the country objects.
- Finds the most crowded country and compares Norway vs. Sweden.
- Prints all results neatly.

---
