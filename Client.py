from Building import Building
from ComparableSorter import ComparableSorter
from ComparableBubbleSorter import ComprableBubbleSorter
import random
class Client:

    def sortByVolumeComparable(self, building_array, sorter : ComparableSorter):
        sorter.sort(building_array)
    def sortByVolumeComparator(self, building_array, sorter):
        pass
    def sortByHeightComparator(self, building_array, sorter):
        pass
 

if __name__ == "__main__":
    client = Client()
    building_array = []
    for i in range(10):
        building_array.append(Building(random.randint(10,200), random.randint(5,500)))
    client.sortByVolumeComparable(building_array, sorter = ComprableBubbleSorter())