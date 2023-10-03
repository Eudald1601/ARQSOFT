from ComparatorSorter import ComparatorSorter

class ComparatorBubbleSorter(ComparatorSorter):
    def sort(self, array):
        n = len(array)
        # Traverse through all array elements
        for i in range(n-1):
        # range(n) also work but outer loop will
        # repeat one time more than needed.
        # Last i elements are already in place
            for j in range(0, n-i-1):
 
        # traverse the array from 0 to n-i-1
        # Swap if the element found is greater
        # than the next element
               
                if self.object.compare(array[j], array[j+1]) >= 0:
                    array[j], array[j + 1] = array[j + 1], array[j]
         
            
        for i in range(n):
            print("Building ", array[i].id, "Volume: ", array[i].volume, "Height: ", array[i].height)