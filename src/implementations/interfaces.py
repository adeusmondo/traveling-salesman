from abc import ABC, abstractmethod
import csv
from typing import List

from src import consts


class Manager(ABC):
    def __init__(self):
        self.distances = consts.DISTANCES_BETWEEN_FICTIONAL_CITIES
        self.cities = consts.CITIES

    def load(self):
        results = []
        with open("../../distancia_entre_capitais_valores.csv") as csvfile:
            reader = csv.reader(csvfile, demiliter=";", quoting=csv.QUOTE_NONNUMERIC_)
            for row in reader:
                results.append(row)

        self.distances = results
        self.cities = [i for i in range(len(results[0]))]

    def calculate_distances(self, solution: List[str]):
        distance = 0

        for i in range(0, len(solution) - 1):
            distance += self.distances[solution[i]][solution[i + 1]]

        distance += self.distances[solution[len(solution) - 1]][solution[0]]

        return distance
    
    @abstractmethod
    def solution(self):
        raise NotImplementedError

