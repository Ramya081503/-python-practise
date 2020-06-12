class Person(object):

    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def basic_details(self):
        print(self.name)
        print(self.idnumber)


class Employee(Person):

    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post

        Person.__init__(self, name, idnumber)

    def official_details(self):
        print(self.salary)
        print(self.post)

a = Employee("ramya", 159, 30000,'software Developer')
a.basic_details()
a.official_details()