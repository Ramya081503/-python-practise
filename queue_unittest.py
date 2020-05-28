import unittest
from queue import Queue


class TestQueue(unittest.TestCase):

    def test_isempty_put1_get1(self):
        q = Queue()
        q.put(10)
        q.get()
        self.assertEqual(True, q.isempty())
        print('queue is empty after 1 put & 1 get items')

    def test_put_get(self):
        q = Queue()
        q.put(5)
        q.put(6)
        self.assertEqual(q.get(), 6)
        self.assertEqual(q.items, [5])
        self.assertEqual(q.size(), 1)
        print('Having 1 item in queue')

    def test_isempty_put_get(self):
        q = Queue()
        q.put(3)
        q.put(1)
        q.get()
        self.assertEqual(False, q.isempty())


if __name__ == '__main__':
    unittest.main()
