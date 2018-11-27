#Raul Rodriguez
#80549657
#Last Modified - 11/26/2018
#Diego Aguirre - Professor
#Anindita Nath - Assistant

class Heap:

    def __init__(self):
        self.heap_array = []

    def insert(self, k):
        self.heap_array.append(k)

    # finds the max value and swaps with min value
    def percolate_down(self, node, heap_list, size):
        child_index = (2 * node) + 1
        element = heap_list[node]

        while child_index < size:
            # Find the max among the node and all the node's children
            max_value = element
            max_index = -1
            i = 0

            while i < 2 and i + child_index < size:
                if heap_list[i + child_index] > max_value:
                    max_value = heap_list[i + child_index]
                    max_index = i + child_index
                i = i + 1

            if max_value == element:
                return
            # swap current node index with max index
            temp = heap_list[node]
            heap_list[node] = heap_list[max_index]
            heap_list[max_index] = temp

            node = max_index
            child_index = 2 * node + 1
            
    def extract_min(self):
        # Returns None if no elements are left in the heap
        if len(self.heap_array) == 0:
            return
        value = self.heap_array[0]
        self.heap_array[0] = self.heap_array[len(self.heap_array)-1]
        del self.heap_array[len(self.heap_array)-1]
        self.percolate_down()
        return value        

    def is_empty(self):
        return len(self.heap_array) == 0   

# Sort the list in ascending order
def heap_sort(heap_list):
    h = Heap()

    i = len(heap_list) // 2 - 1
    while i >= 0:
        h.percolate_down(i, heap_list, len(heap_list))
        i = i - 1

    i = len(heap_list) - 1
    while i > 0:
        # swap
        temp = heap_list[0]
        heap_list[0] = heap_list[i]
        heap_list[i] = temp

        h.percolate_down(0, heap_list, i)
        i = i - 1

# Reads a file and adds each row to it's own list 
def read_file():
    heap_list = []
    file = open("heap_file.txt", "r")
    line = file.read().split(",")

    for num in line:
        heap_list.append(num)

    heap_list = list(map(int, heap_list))

    return heap_list   

def main():
    print("Reading from text file")
    read_list = read_file()
    print("Unsorted: ", read_list)
    heap_sort(read_list)
    print("Sorted: ", read_list)
    
main()    
    
