from Comparable import Comparable

class Building(Comparable):
    
    def __init__(self, volume, height, id):
        self.volume = volume
        self.height = height
        self.id = id      #id to print better the information
    def compare_To(self, o1) -> int:
        if self.volume > o1:
            return 1
        elif self.volume == o1:
            return 0
        else:
            return -1
