from Comparable import Comparable

class ComparableSorter(Comparable):

    def sort(self, array) -> None:
        pass
    
    def compare_To(self, o1, o2) -> int:
        if o1.volume > o2.volume:
            return 1
        elif o1.volume == o2.volume:
            return 0
        else:
            return -1
