
class MaxHeap:

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

    def _getMaxChild(self, i):
        if (i * 2 + 1) > self._size:
            return i * 2

        if self._heap[i*2] > self._heap[i*2 + 1]:
            return i * 2
        else:
            return i * 2 + 1
  
    def _percDown(self, i):
        while i * 2 <= self._size:
            maxChild = self._getMaxChild(i)

            if self._heap[maxChild] > self._heap[i]:
                temp = self._heap[i]
                self._heap[i] = self._heap[maxChild]
                self._heap[maxChild] = temp
            i = maxChild

    def delMaxKey(self):
        if self._size:
            maxValue = self._heap[1]
            self._heap[1] = self._heap[self._size]
            self._size = self._size - 1
            self._heap.pop()
            self._percDown(1)
            return maxValue
        return None

    def _percUp(self, i):
        while i//2 > 0:
            if self._heap[i] > self._heap[i//2]:
                temp = self._heap[i]
                self._heap[i] = self._heap[i//2]
                self._heap[i//2] = temp
            i = i//2

    def insert(self, key):
        if not isinstance(key, self._type):
            raise TypeError("'key' should be of type {}".format(self._type))
    
        self._heap.append(key)
        self._size += 1
        self._percUp(self._size)
        return self

    # Returns the Key with Maximum Value
    def getMaxKey(self):
        return self._heap[1]

    # Creates heap from List of keys
    def createHeapFromList(self, keys=None):

        assert isinstance(keys, list), "'keys' is of type {}, should be of type {}".format(type(keys), list)

        # Checking if all items in 'keys' list are of type self._type
        assert all(isinstance(key, self._type) for key in keys), "All items in 'keys' should be of type {}".format(self._type)

        self._size = len(keys)
        self._heap = [0] + keys[:]
        count = self._size//2

        while count > 0:
            self._percDown(count)
            count -= 1

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

    # Creates a new heap from the list of keys
    def createHeapFromList(self, keys=None):

        assert isinstance(keys, list), "'keys' is of type {}, should be of type {}".format(type(keys), list)

        # Checking if all items in 'keys' list are of type self._type
        assert all(isinstance(key, self._type) for key in keys), "All items in 'keys' should be of type {}".format(self._type)

        self._size = len(keys)
        self._heap = [0] + keys[:]
        count = self._size//2

        while count > 0:
            self._percDown(count)
            count -= 1