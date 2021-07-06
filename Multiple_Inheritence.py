class A():
    def display(self):
        print("Im on A Class")

class B():
    #inherit A
    def display1(self):
        print("Im on B Class")

class C(B,A):
    pass

        #inherit A>
        #inherit B>

   

obj1=C()
obj1.display()

