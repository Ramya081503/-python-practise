import unittest
from sub import Person


class Inherit(unittest.TestCase):

    def test_to_display_the_name_of_the_person(self):
        a = Person("gautham")
        a.getname()
        self.assertEqual(a.getname(), "gautham")

    def test_to_check_subclass_will_inherit_the_super_class_functions(self):
        b = Employee("divya")
        b.getname()
        self.assertEqual(b.getname(), "divya")


if __name__ == '__main__':
    unittest.main()
