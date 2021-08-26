from abc import ABC, abstractmethod


class Manager(ABC):
    @abstractmethod
    def load(self, *file):
        raise NotImplementedError

    @abstractmethod
    def calc_distances(self, cities):
        raise NotImplementedError
    
    @abstractmethod
    def solution(self):
        raise NotImplementedError
