from abc import ABC, abstractmethod
from typing import List

from src import consts


class Manager(ABC):
    def __init__(self):
        self.distances = consts.DISTANCES_BETWEEN_FICTIONAL_CITIES
        self.cities = consts.CITIES

    def load(self, *file):
        if isinstance(file, str):
            raise Exception("This method has not yet been implemented.")
        elif isinstance(file, str):
            raise Exception("This method has not yet been implemented.")
        else:
            raise Exception("Invalid type. Need be a path or file object.")

    def calculate_distances(self, solution: List[str]):
        distance = 0

        for i in range(0, len(solution) - 1):
            distance += self.distances[solution[i]][solution[i + 1]]

        distance += self.distances[solution[len(solution) - 1]][solution[0]]

        return distance
    
    @abstractmethod
    def solution(self):
        raise NotImplementedError

