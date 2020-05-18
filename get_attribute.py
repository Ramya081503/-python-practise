#using getattr function we are calling the attribute of the object:
class Employee:
    employee_id=""
    employee_name=""
    def __init__(self):
        self.employee_id = "105"
        self.employee_name = "ramya"


emp = Employee()
print('field of employee is=',getattr(emp,"emp_field","software"))
try:
    print('field of the employee is =',getattr(emp,"emp_field"))
except AttributeError:
    print("Attribute is not found :(")


