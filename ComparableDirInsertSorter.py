from ComparableSorter import ComparableSorter

class ComparableDirInsertSorter(ComparableSorter):
    def sort(self, array) -> None:

        for step in range(1, len(array)):
            key = array[step]
            j = step - 1
        
        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].        key < array[j]        
            while j >= 0 and self.compare_To(key, array[j]) == -1:
                array[j + 1] = array[j]
                j = j - 1
        
        # Place key at after the element just smaller than it.
            array[j + 1] = key
        for i in range(len(array)):
            print(array[i].volume)
