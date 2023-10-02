from ComparableSorter import ComparableSorter

class ComprableBubbleSorter(ComparableSorter):
    def sort(self, array) -> None:
        n = len(array)
        print("Entro al sort")
        swapped = False
        # Traverse through all array elements
        for i in range(n-1):
        # range(n) also work but outer loop will
        # repeat one time more than needed.
        # Last i elements are already in place
            for j in range(0, n-i-1):
 
        # traverse the array from 0 to n-i-1
        # Swap if the element found is greater
        # than the next element
                
                if self.compare_To(array[j], array[j+1]) >= 0:
                    swapped = True
                    array[j], array[j + 1] = array[j + 1], array[j]
         
                if not swapped:
            # if we haven't needed to make a single swap, we
            # can just exit the main loop.
                    return
                
        for i in range(n-1):
            print(array[i].volume)