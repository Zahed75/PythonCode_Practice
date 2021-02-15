class shape:
    def __init__(self, base,height):
        self.base=base
        self.height=height
    
    def area(self):
        print("im on shape")

class triangle(shape):
    def area(self):
        area=0.5*self.base*self.height
        print("The Triangle Area is",area)

class rectangle(shape):
    def area(self):
        area=self.base*self.height
        print("The Triangle Area is",area)

t1=triangle(3,2)
t1.area()

t1=rectangle(3,2)
t1.area()


    