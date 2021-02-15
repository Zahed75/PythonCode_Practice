class A ():
    def display(self):
        print("Im on A Class")

class B (A):
    #inherit A
    def display1(self):
        print("Im on B Class")

class C (B):
    #inherit B
    def display2(self):
        print("Im on C Class")

obj1=C()
obj1.display()
obj1.display1()
obj1.display2()