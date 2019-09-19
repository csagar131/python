class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.marks = []

    def avg_marks(self):
        return sum(self.marks)/len(self.marks)

class WorkingStudent(Student):
    def __init__(self,name,age,salary):
        super().__init__(name,age)
        self.salary = salary

    @property
    def calc_salary(self):
        return self.salary * 2.0

rolf = WorkingStudent("rolf",21,30000)
rolf.marks.append(14)
rolf.marks.append(20)
print(rolf.avg_marks())
print(rolf.calc_salary)   #  @property decorator added only when need to calculate the value out of functions

