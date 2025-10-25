# Country Stats Project

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
