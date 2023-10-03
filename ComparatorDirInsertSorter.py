from ComparatorSorter import ComparatorSorter

class ComparatorDirInsertSorter(ComparatorSorter):
    def sort(self, array):
        for step in range(1, len(array)):
            key = array[step]
            j = step - 1
        
        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].        key < array[j]        
            while j >= 0 and self.object.compare(key, array[j]) == -1:
                array[j + 1] = array[j]
                j = j - 1
        
        # Place key at after the element just smaller than it.
            array[j + 1] = key
        for i in range(len(array)):
            print("Building ", array[i].id, "Volume: ", array[i].volume, "Height: ", array[i].height)