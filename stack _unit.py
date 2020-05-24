import unittest
from stack import Stack


class TestStack(unittest.TestCase):

    def test_isempty(self):
        s = Stack()
        self.assertEqual(s.size(), 0)

    def test_push(self):
        s = Stack()
        s.push(5)
        s.push(6)
        self.assertEqual(s.items, [5, 6])

    def test_pop(self):
        s = Stack()
        s.push(8)
        s.push(9)
        self.assertEqual(9, s.pop())
        self.assertEqual(8, s.pop())


if __name__ == '__main__':
    unittest.main()
