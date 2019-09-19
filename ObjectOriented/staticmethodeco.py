class Boo:
    @staticmethod # don't need to pass the parameters
    def hi():
        print("i am function without parameter")

print("can be called without defining the object")
Boo.hi()