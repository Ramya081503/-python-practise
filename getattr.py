#using getattr function we are calling the attribute of the object:
class Employee:
    employee_id=""
    employee_name=""
    def __init__(emp):
        emp.employee_id = "50215"
        emp.employee_name = "Gautham"
employee= Employee()
print('Employee id = ',getattr(employee,"employee_id"))
print('Name of the Employee =', getattr(employee, "employee_name"))


