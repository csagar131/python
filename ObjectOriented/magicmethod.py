class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)


ford = Garage()

ford.cars.append("fiesta")
ford.cars.append("focus")
print(len(ford))