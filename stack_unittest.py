import unittest
from stack import Stack


class TestStack(unittest.TestCase):

    def test_isempty_push1_pop1(self):
        s = Stack()
        s.push(5)
        s.pop()
        self.assertEqual(True, s.isempty())
        print('stack is empty')

    def test_push_pop(self):
        s = Stack()
        s.push(8)
        s.push(9)
        self.assertEqual(s.items, [8, 9])
        s.pop()
        self.assertEqual(s.items, [8])
        print('one push one pop succesfully')


if __name__ == '__main__':
    unittest.main()
