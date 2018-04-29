import sys
sys.path.insert(0, '../')

from BinaryHeap import MinHeap

from unittest import TestCase

class TestMinHeap(TestCase):

    def setUp(self):
        self.intHeap1 = MinHeap(dtype=int)
        self.intHeap2 = MinHeap(dtype=int)

        self.intHeap1.insert(5).insert(4).insert(3).insert(2).insert(1)
        self.intHeap2.insert(1).insert(2).insert(3).insert(4).insert(5)

    def test_heapSize(self):
        self.assertEqual(self.intHeap1.getSize(), 5)
        self.assertEqual(self.intHeap2.getSize(), 5)

    def test_getMinimumKey(self):
        self.assertEqual(self.intHeap1.getMinKey(), 1)
        self.assertEqual(self.intHeap1.getMinKey(), 1)

    def test_deleteMinKey(self):
        self.assertEqual(self.intHeap1.delMinKey(), 1)
        self.assertEqual(self.intHeap1.delMinKey(), 2)
        self.assertEqual(self.intHeap1.delMinKey(), 3)
        self.assertEqual(self.intHeap1.delMinKey(), 4)
        self.assertEqual(self.intHeap1.delMinKey(), 5)
        self.assertEqual(self.intHeap1.delMinKey(), None)

        self.assertEqual(self.intHeap2.delMinKey(), 1)
        self.assertEqual(self.intHeap2.delMinKey(), 2)
        self.assertEqual(self.intHeap2.delMinKey(), 3)
        self.assertEqual(self.intHeap2.delMinKey(), 4)
        self.assertEqual(self.intHeap2.delMinKey(), 5)
        self.assertEqual(self.intHeap2.delMinKey(), None)

    def tearDown(self):
        del self.intHeap1
        del self.intHeap2

if __name__ == '__main__':
    unittest.main()