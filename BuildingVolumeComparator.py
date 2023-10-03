from Comparator import Comparator

class BuildingVolumeComparator(Comparator):
    def compare(self, o1, o2) -> int:
        if o1.volume > o2.volume:
            return 1
        elif o1.volume == o2.volume:
            return 0
        else:
            return -1