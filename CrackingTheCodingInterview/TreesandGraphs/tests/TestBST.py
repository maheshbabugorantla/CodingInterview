import sys
sys.path.insert(0, '../')

from BST import BST

from unittest import TestCase

class TestBST(TestCase):
    def setUp(self):
        self.list1 = [3, 2, 1, 5, 6, 7]

        # Creating the BST1
        self.BST1 = BST(dtype=int, key=4)

        for val in self.list1:
              self.BST1 = self.BST1.insert(val)

    def test_insert(self):
        self.assertEqual(self.BST1.key, 4)
        self.assertEqual(self.BST1.left.key, 3)
        self.assertEqual(self.BST1.right.key, 5)

        self.BST1 = self.BST1.insert(9)
        self.assertEqual(self.BST1.right.right.right.right.key, 9)

    def test_preOrderTraversal(self):
        preOrderValues = [4, 3, 2, 1, 5, 6, 7]
        self.assertEqual(self.BST1.PreOT(), ', '.join(str(i) for i in preOrderValues))

    def test_inOrderTraversal(self):
        inOrderValues = [1,2,3,4,5,6,7]
        self.assertEqual(self.BST1.IOT(), ', '.join([str(i) for i in inOrderValues]))

    def test_postOrderTraversal(self):
        postOrderValues = [1, 2, 3, 7, 6, 5, 4]
        self.assertEqual(self.BST1.PostOT(), ', '.join([str(i) for i in postOrderValues]))

    def tearDown(self):
        del self.list1

if __name__=='__main__':
    unittest.main()