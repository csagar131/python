# public => memberName
# protected => _memberName
# private => __memberName


class Car:
    numberOfWheels = 4
    _color = "black"
    __yearOfManufacture = 2017     #_Car_yearOfManufacture     name mangling internally


class Bmw(Car):
    def __init__(self):
        print("protected attribute color {}".format(self._color))



car = Car()
print("public attribute numberOfWheels:",car.numberOfWheels)
bmw = Bmw()
print("private attribute yearOfManufacture:",car._Car_yearOfManufacture)  #not recommended



