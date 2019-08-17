class A:
    def method(self):
        print("from class A")

class B(A):
    def method(self):
        print("from class B")

class C(A):
    def method(self):
        print("from class C")
    
class D(B,A):   # the class inherited first will given the preference
    pass


d = D()           
d.method()    # prints method from class B     
