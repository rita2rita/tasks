import unittest
from LinkedList import LinkedList


class LinkedListTestBase(unittest.TestCase):
    # """ Base class fore tests of QueueFifo implementations. """

    def _create_list(self) -> LinkedList:
        """ Create QueueFifo implementation object """
        raise NotImplementedError

    def test_equeue(self):
        queue = self._create_list()
        queue.add(0, 1)
        queue.add(1, 2)
        queue.add(0, 3)
        queue.add(1, 4)
        self.assertEqual(queue.get(1), 4)
        queue.add(2, 5)
        queue.add(4, 6)
        queue.add(5, 7)
        queue.add_last(100)
        queue.add_first(111)
        self.assertEqual(queue.count(), 9)
        queue.get(2)
        self.assertEqual(queue.get(2), 4)
        self.assertEqual(queue.get(1), 3)
        self.assertEqual(queue.get(7), 2)
        self.assertEqual(queue.get(0), 111)
        self.assertEqual(queue.get(8), 100)

    def test_add_first(self):
        queue = self._create_list()
        queue.add_first(1)
        self.assertEqual(queue.get(0), 1)
        queue.add_first(2)
        self.assertEqual(queue.get(0), 2)
        queue.add_first(3)
        self.assertEqual(queue.get(0), 3)
        queue.add_first(4)
        self.assertEqual(queue.get(0), 4)

    def test_add_last(self):
        queue = self._create_list()
        queue.add_last(1)
        self.assertEqual(queue.get(0), 1)
        queue.add_last(2)
        self.assertEqual(queue.get(1), 2)
        queue.add_last(3)
        self.assertEqual(queue.get(2), 3)
        queue.add_last(4)
        self.assertEqual(queue.get(3), 4)

    def test_remove(self):
        queue = self._create_list()
        queue.add_last(1)
        queue.add_last(2)
        queue.add_last(3)
        queue.add_last(4)
        queue.remove(0)
        self.assertEqual(queue.get(0), 2)
        queue.remove(1)
        self.assertEqual(queue.get(1), 4)