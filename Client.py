from Building import Building
from ComparableSorter import ComparableSorter
from ComparableBubbleSorter import ComprableBubbleSorter
from ComparableDirInsertSorter import ComparableDirInsertSorter
from ComparatorBubbleSorter import ComparatorBubbleSorter


from ComparatorDirInsertSorter import ComparatorDirInsertSorter
from ComparatorSorter import ComparatorSorter
from BuildingVolumeComparator import BuildingVolumeComparator
from BuildingHeightComparator import BuildingHeightComparator
import random
class Client:

    def sortByVolumeComparable(self, building_array, sorter : ComparableSorter):
        sorter.sort(building_array)
    def sortByVolumeComparator(self, building_array, sorter: ComparatorSorter):
        sorter.sort(building_array)
    def sortByHeightComparator(self, building_array, sorter: ComparatorSorter):
        sorter.sort(building_array)
 

if __name__ == "__main__":
    client = Client()
    building_array = []
    for i in range(10):
        building_array.append(Building(random.randint(10,200), random.randint(5,500), i))
        print("Building",i , ": Volume:", building_array[i].volume, " Height:", building_array[i].height)
    print("\nBubble Comparable")
    client.sortByVolumeComparable(building_array, sorter = ComprableBubbleSorter())
    print("\nDir Insert Comparable")
    client.sortByVolumeComparable(building_array, sorter = ComparableDirInsertSorter() )
    print("\nBubble Volume Comparator")
    client.sortByVolumeComparator(building_array, sorter = ComparatorBubbleSorter(BuildingVolumeComparator()))
    print("\nDir Insert Volume Comparator")
    client.sortByVolumeComparator(building_array, sorter = ComparatorDirInsertSorter(BuildingVolumeComparator()))
    print("\nBubble Height Comparator")
    client.sortByHeightComparator(building_array, sorter = ComparatorBubbleSorter(BuildingHeightComparator()))
    print("\nDir Insert Height Comparator")
    client.sortByHeightComparator(building_array, sorter = ComparatorDirInsertSorter(BuildingHeightComparator()))