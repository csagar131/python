class Employee:
    def numberOfWorkingHour(self):
        self.numberHour = 45

    def showHour(self):
        print(self.numberHour)

class Trainee(Employee):
    def numberOfWorkingHour(self):
        self.numberHour = 40
    
    def resetHours(self):
        super().numberOfWorkingHour()

    
e = Employee()
e.numberOfWorkingHour()
print("show hour:",end=' ')
e.showHour()

t = Trainee()
t.numberOfWorkingHour()
print("show hour from trainee:",end=' ')
t.showHour()

print("after resetting the hour",end=' ')
t.resetHours()
t.showHour()


    
