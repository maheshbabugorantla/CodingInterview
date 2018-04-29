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

        self.intHeap1.insert(1).insert(2).insert(3).insert(4).insert(5)
        self.intHeap2.insert(10).insert(9).insert(8).insert(20).insert(21).insert(12)

        self.strHeap1.insert('Blah1').insert('Blah2').insert('Foo').insert('Bar')
        self.strHeap2.insert('What').insert('does').insert('fox').insert('say')

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

    def tearDown(self):
        del self.intHeap1
        del self.intHeap2
        del self.strHeap1
        del self.strHeap2

if __name__ == '__main__':
    unittest.main()