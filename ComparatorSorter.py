from abc import ABC, abstractmethod
from Comparator import Comparator

class ComparatorSorter(ABC, Comparator):
    def __init__(self, object: Comparator):
        self.object = object

    @abstractmethod
    def sort(self, array):
        pass