class Student:
    student_id = "12345"
    student_name="ramya"
    def show(self):
        print(self.student_id)
        print(self.student_name)
s=Student()
print(getattr(s,'student_name'))
#has attr will check if there is an attribute or not which we specified:
print(hasattr(s,'rollnumber'))
setattr(s,'rollnumber',48)
print(getattr(s,'rollnumber'))
delattr(Student,'student_id')