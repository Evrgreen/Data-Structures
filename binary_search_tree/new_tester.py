import unittest
from binary_search_tree import BSTNode


class BinarySearchTreeTest(unittest.TestCase):
    def setUp(self):
        self.root = BSTNode(5)

    def test_inserts_lower_to_left(self):
        self.root.insert(4)
        self.assertEqual(self.root.left.value, 4)

    def test_inserts_higher_to_right(self):
        self.root.insert(6)
        self.assertEqual(self.root.right.value, 6)

    def test_deep_insertion_path(self):
        self.root.insert(2)
        self.root.insert(4)
        self.root.insert(3)
        self.assertEqual(self.root.left.right.left.value, 3)


if __name__ == "__main__":
    unittest.main()
