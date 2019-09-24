class Car:
    def __init__(self,make,model):
        self.make = make
        self.model =  model


class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)
    
    def add_cars(self,car):
        if not isinstance(car,Car):
            # raising a type error if car is not of type class Car
            raise TypeError(f'Tried to add of type `{car.__class__.__name__}`, need `Car` type')
        self.cars.append(car)




ford = Garage()
car1 = Car("ford","fiesta")
car2 =  Car("mercedes","benz")
ford.add_cars(car1)
ford.add_cars(car2)
print(len(ford))
print(ford.cars)



#Traceback (most recent call last):
##  File ".\TypeErraise.py", line 25, in <module>
#    ford.add_cars("audi")
#  File ".\TypeErraise.py", line 17, in add_cars
#    raise TypeError(f'Tried to add str `{car.__class__.__name__}`, need `Car` type')
#TypeError: Tried to add str `str`, need `Car` type
#PS D:\Udemy\python\ErrorHandling> python .\TypeErraise.py
#Traceback (most recent call last):
#  File ".\TypeErraise.py", line 25, in <module>
#    ford.add_cars(car)
#  File ".\TypeErraise.py", line 18, in add_cars
#    self.cars.add(car)
#AttributeError: 'list' object has no attribute 'add'
#PS D:\Udemy\python\ErrorHandling> python .\TypeErraise.py
#1
#PS D:\Udemy\python\ErrorHandling> python .\TypeErraise.py
#1
#[<__main__.Car object at 0x000001FB072D19E8>]
#PS D:\Udemy\python\ErrorHandling> python .\TypeErraise.py
#2
#[<__main__.Car object at 0x00000202659E19E8>, <__main__.Car object at 0x00000202659E1CF8>]