from Comparator import Comparator

class BuildingHeightComparator(Comparator):
    def compare(self, o1, o2) -> int:
        if o1.height > o2.height:
            return 1
        elif o1.height == o2.height:
            return 0
        else: 
            return -1
        