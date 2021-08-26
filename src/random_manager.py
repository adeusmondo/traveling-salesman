from random import randint

from src.interfaces import Manager

class TravelerManager(Manager):
    def __init__(self):
        self.cities = ["A", "B", "C", "D", "E"]
        self.distances = {
            "A": {
                "A": 0, 
                "B": 2, 
                "C": 4, 
                "D": 3,
                "E": 4,
            }, 
            "B": {
                "A": 2,
                "B": 0,
                "C": 1,
                "D": 1,
                "E": 3,
            }, 
            "C": {
                "A": 4,
                "B": 1,
                "C": 0,
                "D": 5,
                "E": 8,
            },
            "D": {
                "A": 3,
                "B": 1,
                "C": 5,
                "D": 0,
                "E": 2,
            },
            "E": {
                "A": 4,
                "B": 2,
                "C": 8,
                "D": 2,
                "E": 2,                                                                                                   
            },
    
        }
        self.solution = []

    def load(self, *file):
        pass

    def random_solution(self):
        cities_copy = self.cities.copy()
        random_sort = []

        while len(cities_copy) > 0:
            random_number = randint(0 , len(cities_copy)) - 1
            city_pop = cities_copy.pop(random_number)
            random_sort.append(city_pop)

        return random_sort

    def calculate_distances(self, cities):
        previus_city = None
        next_city = None
        for city in cities:
            pass

        pass

