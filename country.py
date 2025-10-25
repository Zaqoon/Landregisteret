

class Country:  # Task a)
    def __init__(self, name, population=0, area=0):
        self.name = name
        self.population = population
        self.area = area

    def __str__(self):  # Task b)
        self.calculate_population_density()
        if self.population_density is not None:
            return f'Name: {self.name}\nPopulation: {self.population}\nArea: {self.area}\nPopulation Density: {self.population_density}'
        else:
            return f'Name: {self.name}\nPopulation: {self.population}\nArea: {self.area}'

    def calculate_population_density(self):  # Task c)
        if self.area and self.population:
            self.population_density = round(self.population / self.area, 2)
        else:
            self.population_density = None

        return self.population_density


if __name__ == '__main__':
    c = Country('Norway')
    print(c)
