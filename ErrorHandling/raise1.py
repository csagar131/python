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

