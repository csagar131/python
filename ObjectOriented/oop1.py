class Student:
    def __init__(self,new_name,new_marks):
        self.name = new_name
        self.marks = new_marks

    def calc_avg(self):
        return sum(self.marks)/len(self.marks)

    
student_one = Student("jose",[2,4,3,5])

print(student_one.name)