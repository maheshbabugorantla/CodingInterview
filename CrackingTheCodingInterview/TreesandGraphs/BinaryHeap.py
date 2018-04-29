
class MaxHeap:

    def __init__(self, dtype=None):

        if dtype is None:
            raise ValueError("'type' cannot be None")
        
        if not isinstance(dtype, type):
            raise TypeError("'dtype' should be of type <class 'type'>")

        self._type = dtype
        self._heap = [None]
        self._size = 0

    # This percolates the Maximum Key
    def _percDown(self, i):
        pass

    def insert(self, key):
        pass

class MinHeap:

    def __init__(self, dtype=None):

        if dtype is None:
            raise ValueError("'type' cannot be None")
        
        if not isinstance(dtype, type):
            raise TypeError("'dtype' should be of type <class 'type'>")

        self._type = dtype
        self._heap = [None]
        self._size = 0

    def getSize(self):
        return self._size

    def insert(self, key):
        if not isinstance(key, self._type):
            raise TypeError("key should of be of type {}".format(self._type))
        self._size += 1
        self._heap.append(key)
        self._percUp(self._size)
        return self

    def _percUp(self, i):
        while i//2 > 0:
            if self._heap[i] < self._heap[i//2]:
                tmp = self._heap[i//2]
                self._heap[i//2] = self._heap[i]
                self._heap[i] = tmp
            i = i//2

    # Returns the key with minimum value
    def getMinKey(self):
        return self._heap[1]

    def _percDown(self, i):
        while (i * 2) <= self._size:
            minChild = self._getMinChild(i)
            if self._heap[minChild] < self._heap[i]:
                temp = self._heap[minChild]
                self._heap[minChild] = self._heap[i]
                self._heap[i] = temp
            i = minChild

    # Returns the Index of the Min Child
    def _getMinChild(self, i):

        if (i * 2 + 1) > self._size:
            return i * 2
        else:
            if self._heap[i * 2] < self._heap[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    # Deletes the Min Key and returns the minimum key
    def delMinKey(self):
        if self._size:
            minVal = self._heap[1]
            self._heap[1] = self._heap[self._size]
            self._size = self._size - 1
            self._heap.pop()
            self._percDown(1)
            return minVal
        return None