import  unittest
import calc


class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(5,4),9)
        self.assertEqual(calc.add(5,1),6)
        self.assertEqual(calc.add(5,8),13)
        self.assertEqual(calc.add(8,8),16)
    def test_subtract(self):
        self.assertEqual(calc.subtract(5,8),-3)
        self.assertEqual(calc.subtract(4,2),2)
        self.assertEqual(calc.subtract(9,3),6)
        self.assertEqual(calc.subtract(8,1),7)

    def test_multiply(self):
        self.assertEqual(calc.multiply(5,8),40)
        self.assertEqual(calc.multiply(4,2),8)
        self.assertEqual(calc.multiply(9,3),27)
        self.assertEqual(calc.multiply(8,1),8)

if __name__ == '__main__':
    unittest.main()