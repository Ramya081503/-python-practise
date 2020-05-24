import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self):
        print('setUp')
        self.emp_1 = Employee('ramya', 'koppolu', 30000)
        self.emp_2 = Employee('divya', 'gautham', 50000)

    def tearDown(self):
        print('tearDown')

    def test_email(self):
        print('test_email')
        self.assertEqual(self.emp_1.email, 'ramya.koppolu@email.com')
        self.assertEqual(self.emp_2.email, 'divya.gautham@email.com')

        self.emp_1.first = 'parvathi'
        self.emp_2.first = 'jhansi'

        self.assertEqual(self.emp_1.email, 'parvathi.koppolu@email.com')
        self.assertEqual(self.emp_2.email, 'jhansi.gautham@email.com')

    def test_fullname(self):
        print('test_fullname')
        self.assertEqual(self.emp_1.fullname, 'ramya koppolu')
        self.assertEqual(self.emp_2.fullname, 'divya gautham')

        self.emp_1.first = 'parvathi'
        self.emp_2.first = 'jhansi'

        self.assertEqual(self.emp_1.fullname, 'parvathi koppolu')
        self.assertEqual(self.emp_2.fullname, 'jhansi gautham')


if __name__ == '__ main__':
    unittest.main()
