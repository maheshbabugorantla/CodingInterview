import sys
sys.path.insert(0, '../')

from BinaryHeap import MaxHeap

from unittest import TestCase

class TestMaxHeap(TestCase):

    def setUp(self):
        self.intHeap1 = MaxHeap(dtype=int)
        self.intHeap2 = MaxHeap(dtype=int)

        self.strHeap1 = MaxHeap(dtype=str)
        self.strHeap2 = MaxHeap(dtype=str)

        self.intHeap1.createHeapFromList(keys=[1, 2, 3, 4, 5])
        self.intHeap2.createHeapFromList(keys=[10, 9, 8, 20, 21, 12])

        self.strHeap1.createHeapFromList(keys=['Blah1', 'Blah2', 'Foo', 'Bar'])
        self.strHeap2.createHeapFromList(keys=['What', 'does', 'fox', 'say'])

    def test_getSize(self):
        self.assertEqual(self.intHeap1.getSize(), 5)
        self.assertEqual(self.intHeap2.getSize(), 6)

        self.assertEqual(self.strHeap1.getSize(), 4)
        self.assertEqual(self.strHeap2.getSize(), 4)

    def test_getMaxKey(self):

        self.assertEqual(self.intHeap1.getMaxKey(), 5)
        self.assertEqual(self.intHeap2.getMaxKey(), 21)

        self.assertEqual(self.strHeap1.getMaxKey(), 'Foo')
        self.assertEqual(self.strHeap2.getMaxKey(), 'say')
 
        self.intHeap1.insert(25).insert(30).insert(35)
        self.intHeap2.insert(50).insert(49).insert(20)

        self.strHeap1.insert('Blah1111').insert('Blah2113q43242').insert('Foo111').insert('Bar43fsdfa').insert('Foo1234')
        self.strHeap2.insert('What').insert('does').insert('fox').insert('say')

        self.assertEqual(self.intHeap1.getMaxKey(), 35)
        self.assertEqual(self.intHeap2.getMaxKey(), 50)

        self.assertEqual(self.strHeap1.getMaxKey(), 'Foo1234')
        self.assertEqual(self.strHeap2.getMaxKey(), 'say')

    def test_delMaxKey(self):
        self.assertEqual(self.intHeap1.delMaxKey(), 5)
        self.assertEqual(self.intHeap1.delMaxKey(), 4)
        self.assertEqual(self.intHeap1.delMaxKey(), 3)
        self.assertEqual(self.intHeap1.delMaxKey(), 2)
        self.assertEqual(self.intHeap1.delMaxKey(), 1)
        self.assertEqual(self.intHeap1.delMaxKey(), None)

        self.assertEqual(self.intHeap2.delMaxKey(), 21)
        self.assertEqual(self.intHeap2.delMaxKey(), 20)
        self.assertEqual(self.intHeap2.delMaxKey(), 12)
        self.assertEqual(self.intHeap2.delMaxKey(), 10)
        self.assertEqual(self.intHeap2.delMaxKey(), 9)
        self.assertEqual(self.intHeap2.delMaxKey(), 8)
        self.assertEqual(self.intHeap2.delMaxKey(), None)

    def tearDown(self):
        del self.intHeap1
        del self.intHeap2
        del self.strHeap1
        del self.strHeap2

if __name__ == '__main__':
    unittest.main()