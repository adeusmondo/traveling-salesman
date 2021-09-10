from random import randint, randrange

from src.implementations.interfaces import Manager

class TravelerManager(Manager):
    def __init__(self):
        super().__init__()
        self.delta = 75

    def solution(self):
        cities_copy = self.cities.copy()
        random_number = randint(0 , len(cities_copy)) - 1
        starter_city = cities_copy[random_number]
        del cities_copy[random_number]
        semi_greedy_sort = [starter_city]

        while len(cities_copy) > 0:
            random_value = randrange(100)

            if self.delta > random_value:
                # Método Guloso
                city_leaving = self.cities[semi_greedy_sort[len(semi_greedy_sort) - 1]]
                nearest_city = cities_copy[0]
                nearest_city_idx = 0
                shortest_distance = self.distances[city_leaving][nearest_city]
                idx = 0

                for possible_next_city in cities_copy:
                    distance = self.distances[city_leaving][possible_next_city]
                    if distance < shortest_distance:
                        shortest_distance = distance
                        nearest_city = possible_next_city
                        nearest_city_idx = idx
                    idx += 1

                city_pop = cities_copy.pop(nearest_city_idx)
                semi_greedy_sort.append(city_pop)
            else:
                # Método Aleátorio
                random_number = randint(0, len(cities_copy)) - 1
                city_pop = cities_copy.pop(random_number)
                semi_greedy_sort.append(city_pop)

        return semi_greedy_sort

