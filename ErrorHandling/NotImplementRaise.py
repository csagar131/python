class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)
    
    def add_cars(self,cars):
        raise NotImplementedError("This method has not Implemented yet")

ford = Garage()
ford.add_cars("audi")
print(len(ford))



##Traceback (most recent call last):
 # File ".\NotImplementRaise.py", line 12, in <module>
#    ford.add_cars("audi")
#  File ".\NotImplementRaise.py", line 9, in add_cars
##    raise NotImplementedError("This method has not Implemented yet")
#NotImplementedError: This method has not Implemented yet