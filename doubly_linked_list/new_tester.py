import unittest
from doubly_linked_list import DoublyLinkedList, ListNode


class DLList(unittest.TestCase):
    def setUp(self):
        self.node = ListNode(1)
        self.dll = DoublyLinkedList(self.node)

    def test_add_to_head(self):
        self.assertEqual(self.dll.head.value, 1)
        self.dll.add_to_head(10)
        self.assertEqual(self.dll.head.value, 10)
        self.assertEqual(self.dll.head.next.value, 1)

    def test_add_to_empty_list(self):
        self.dll.remove_from_head()
        self.assertIsNone(self.dll.head)
        self.assertIsNone(self.dll.tail)
        self.dll.add_to_head(10)
        self.assertEqual(self.dll.head.value, 10)
        self.assertEqual(self.dll.tail.value, 10)
        self.assertIsNone(self.dll.head.next, 10)

    def test_len(self):
        self.assertEqual(len(self.dll), 1)
        self.dll.add_to_head(10)
        self.assertEqual(len(self.dll), 2)
        self.dll.add_to_head(30)
        self.dll.add_to_head(20)
        self.assertEqual(len(self.dll), 4)
        self.dll.remove_from_head()
        self.assertEqual(len(self.dll), 3)

    def test_remove_from_head_with_one_item(self):

        self.assertEqual(self.dll.head.value, 1)
        self.assertEqual(self.dll.remove_from_head(), 1)
        self.assertIsNone(self.dll.head)
        self.assertIsNone(self.dll.tail)
        self.assertEqual(len(self.dll), 0)

    def test_remove_from_head_with_multi_item(self):
        self.assertEqual(self.dll.head.value, 1)
        self.dll.add_to_head(20)
        self.dll.add_to_head(20)
        self.dll.add_to_head(40)
        self.assertEqual(self.dll.remove_from_head(), 40)
        self.assertIsNone(self.dll.head.prev)
        self.assertEqual(len(self.dll), 3)


if __name__ == "__main__":
    unittest.main()
