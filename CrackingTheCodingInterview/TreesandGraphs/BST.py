
class BST:

    def __init__(self, dtype=None, key=None):

        if not dtype:
            raise ValueError("'dtype' cannot be None")

        if not isinstance(dtype, type):
            raise TypeError("'dtype' should be of type <class 'type'>")

        if key is None:
            raise ValueError("'key' cannot be None")
        
        if not isinstance(key, dtype):
            raise TypeError("'key' should be of type {}".format(dtype))

        self.type = dtype
        self.key = key
        self.left = None
        self.right = None

    def insertLeft(self, key):
        if not self.left:
            return BST(dtype=self.type, key=key)

        self.left.insert(key)
        return self.left

    def insertRight(self, key):
        if not self.right:
            return BST(dtype=self.type, key=key)

        self.right.insert(key)
        return self.right

    def insert(self, key):

        if not isinstance(key, self.type):
            raise TypeError("'key' should be of type {}".format(self.type))

        if key < self.key:
            self.left = self.insertLeft(key)

        elif key > self.key:
            self.right = self.insertRight(key)

        return self

    # In-Order Traversal Helper Function
    def _IOT(self, iotList=None, root=None):

        if not root:
            return iotList

        # Left
        iotList = self._IOT(iotList=iotList, root=root.left)

        # Root
        iotList.append(root.key)

        # Right
        iotList = self._IOT(iotList=iotList, root=root.right)

        return iotList

    # In-Order Traversal
    def IOT(self):
        _iot = list()
        _iot = self._IOT(_iot, root=self)
        return ', '.join([str(i) for i in _iot])

    # Pre-Order Traversal Helper Function
    def _PreOT(self, preotList=None, root=None):

        if not root:
            return preotList

        # Root
        preotList.append(root.key)

        # Left
        preotList = self._PreOT(preotList=preotList, root=root.left)

        # Right
        preotList = self._PreOT(preotList=preotList, root=root.right)

        return preotList

    # Pre-Order Traversal
    def PreOT(self):
        _preot = list()
        _preot = self._PreOT(preotList=_preot, root=self)
        return ', '.join([str(i) for i in _preot])

    # Post-Order Traversal Helper Function
    def _PostOT(self, postotList=None, root=None):

        if not root:
            return postotList

        # Left
        postotList = self._PostOT(postotList=postotList, root=root.left)

        # Right
        postotList = self._PostOT(postotList=postotList, root=root.right)

        # Root
        postotList.append(root.key)

        return postotList

    # Post-Order Traversal
    def PostOT(self):
        _postot = list()
        _postot = self._PostOT(postotList=_postot, root=self)
        return ', '.join([str(i) for i in _postot])
