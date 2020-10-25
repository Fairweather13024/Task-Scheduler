'''
Thiscode is adapted from the Pre class work of the Heaps and Heapsort session.
Here I initialize a class that implements the min-heap functionalities of a priority queue.
The class only has two attributes - The heap, and the heap_size
'''

def left(i):
    '''
    Returns the left child of the parent at index i
    '''
    return 2 * i + 1


def right(i):
    '''
    Returns the right child of the parent at index i
    '''
    return 2 * i + 2


def parent(i):
    '''
    Returns the parent of the child node at i
    '''
    return (i - 1) // 2


class MinHeapq:

    def __init__ (self, heap = []):

        """
        Declaring class attributes

        """
        print('see what heap has been passed as', heap)
        self.heap = heap     #This is the heap that I will pas as an argument
        self.heap_size = len(heap)     #This is teh heap size


    def mink (self):
        """
        This method returns the smallest key in the priority queue

        """
        return self.heap[0]     #Returns teh root node

    def heappush(self, key):
        """
        Inserts the value of key onto the priority queue, maintaining the
        min heap invariant.

        """
        self.heap.append(float("inf"))  # inf ensures that there are always values less than it
        self.decrease_key(self.heap_size, key)
        self.heap_size += 1

    def decrease_key(self, i, key):
        """
        Modifies the value of the key in the heap with a lower value

        """
        if key[0] > self.heap[i]:  # the key must be smaller for the min heap attribute to hold
            raise ValueError('New key is bigger than the current key')
        self.heap[i] = key
        while i > 0 and self.heap[parent(i)][0] > self.heap[i][0]:    #
            j = parent(i)
            holder = self.heap[j]
            self.heap[j] = self.heap[i]
            self.heap[i] = holder
            i = j

    def heapify(self, i = 0):
        """
        This method implements the MAX_HEAPIFY operation for the max priority
        queue. The input is the array index of the root node of the subtree to
        be heapify.

        """
        l = left(i)
        r = right(i)
        heap = self.heap

        if l <= (self.heap_size - 1) and heap[l] < heap[i]:
            smallest = l
        else:
            smallest = i
        if r <= (self.heap_size - 1) and heap[r] < heap[smallest]:
            smallest = r
        if smallest != i:
            heap[i], heap[smallest] = heap[smallest], heap[i]
            self.heapify(smallest)

    def heappop(self):
        """
        This method implements the EXTRACT_MAX operation. It returns the largest
        key in the max priority queue and removes this key from the max priority
        queue.

        """
        if self.heap_size < 1:
            raise ValueError('Heap underflow: There are no keys in the priority queue ')
        mink = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.heap_size -= 1
        self.heapify(0)
        return mink


