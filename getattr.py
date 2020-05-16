#using getattr function we are calling the attribute of the object:
class Employee:
    Employee_id=""
    Employee_name=""
    def __init__(emp):
        emp.Employee_id = "D1056"
        emp.Employee_name = "Ramya"


Employee = Employee()
print('Employee id =',getattr(Employee,"Employee_id"))
print('Name of the Employee =', getattr(Employee, "Employee_name"))


