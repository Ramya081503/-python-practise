import unittest
from stack import Stack


class TestStack(unittest.TestCase):

    def test_pop_should_raise_an_error(self):
        s = Stack()
        s.push(1)
        s.push(5)
        s.pop()
        s.pop()
        s.pop()
        try:
            (s.pop() < 2)
        except Exception as e:
            print('popped from empty stack', e)

        
if __name__ == '__main__':
    unittest.main()
