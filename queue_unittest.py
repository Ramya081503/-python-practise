import unittest
from queue import Queue


class TestQueue(unittest.TestCase):

    def test_isempty(self):
        q = Queue()
        self.assertEqual(q.size(), 0)

    def test_put(self):
        q = Queue()
        q.put(5)
        q.put(6)
        self.assertEqual(q.items, [5, 6])

    def test_get(self):
        q = Queue()
        q.put(8)
        q.put(9)
        self.assertEqual(9, q.get())
        self.assertEqual(8, q.get())


if __name__ == '__main__':
    unittest.main()
