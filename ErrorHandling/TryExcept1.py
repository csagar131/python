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
            raise ValueError(f'Tried to add of type `{car.__class__.__name__}`, need `{Car}` type')
        self.cars.append(car)


fiesta = Car("ford","fiesta")
obj = Garage()
try:
    obj.add_cars("fiesta")
except TypeError:
    print("hii am TypeError")
except ValueError:   # value error handled here if not written this line will handled above
    print("hii am ValueError")
finally:
    print(f' cars length is {len(obj.cars)}')