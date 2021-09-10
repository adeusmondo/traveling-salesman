from random import randint

from src.implementations.interfaces import Manager

class TravelerManager(Manager):
    def __init__(self):
        super().__init__()

    def solution(self):
        cities_copy = self.cities.copy()
        random_sort = []

        while len(cities_copy) > 0:
            random_number = randint(0 , len(cities_copy)) - 1
            city_pop = cities_copy.pop(random_number)
            random_sort.append(city_pop)

        return random_sort

