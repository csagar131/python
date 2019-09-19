class Foo:
    @classmethod
    def hi(cls):    # insted of taking self as object takes the classname
        print(cls.__name__)

k = Foo()
k.hi()
print("can be called through the class name")
Foo.hi()