import unittest
from QueueFifo import QueueFifo


class QueueFifoTest(unittest.TestCase):
    def test_dequeue(self):
        queue = QueueFifo(4)
        queue.equeue(0)
        queue.equeue(1)
        queue.equeue(2)
        queue.equeue(3)
        self.assertEqual(queue.dequeue(), 0)
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.dequeue(), 2)
        self.assertEqual(queue.dequeue(), 3)

    def test_too_much_dequeue(self):
        queue = QueueFifo(10)
        queue.equeue(0)
        self.assertEqual(queue.dequeue(), 0)
        self.assertRaises(Exception, lambda: queue.dequeue())

    def test_count(self):
        queue = QueueFifo(4)
        queue.equeue(0)
        queue.equeue(1)
        queue.equeue(2)
        queue.equeue(3)
        self.assertEqual(queue.count(), 4)

    def test_overflow(self):
        queue = QueueFifo(2)
        queue.equeue(0)
        queue.equeue(1)
        self.assertRaises(Exception, lambda: queue.equeue(2))

    def test_max_size_1(self):
        queue = QueueFifo(1)
        queue.equeue(0)
        with self.assertRaises(Exception):
            queue.equeue(1)

    def test_max_size_3(self):
        queue = QueueFifo(3)
        queue.equeue(0)
        queue.equeue(1)
        queue.equeue(2)
        self.assertRaises(Exception, lambda: queue.equeue(3))

    def test_intensive(self):
        queue = QueueFifo(3)
        queue.equeue(0)
        queue.equeue(1)
        self.assertEqual(queue.dequeue(), 0)
        self.assertEqual(queue.dequeue(), 1)
        queue.equeue(2)
        queue.equeue(3)
        queue.equeue(4)
        self.assertEqual(queue.dequeue(), 2)
        self.assertEqual(queue.dequeue(), 3)
        queue.equeue(5)
        self.assertEqual(queue.dequeue(), 4)
        queue.equeue(6)
        self.assertEqual(queue.dequeue(), 5)
        queue.equeue(7)
        self.assertEqual(queue.dequeue(), 6)
        self.assertEqual(queue.dequeue(), 7)


if __name__ == '__main__':
    unittest.main()
