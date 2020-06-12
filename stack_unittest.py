import unittest
from stack import Stack


class TestStack(unittest.TestCase):

    def test_pop_from_empty_stack_raising_an_error(self):
        s = Stack()
        s.push(2)
        s.push(4)
        s.pop()
        s.pop()
        s.pop()



if __name__ == '__main__':
    unittest.main()
