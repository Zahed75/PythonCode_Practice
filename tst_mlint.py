class A ():
    def display(self):
        print("Im on A Class")

class B ():
    #inherit A
    def display1(self):
        print("Im on B Class")

class C (A,B):
      pass
 
        #inherit A>
        #inherit B>

   

obj1=C()
obj1=C.display()
