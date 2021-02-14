class traingle():
    def __init__(self, height, base):
        self.height=height
        self.base=base
    
    def calculate_area(self):
        area=0.5*self.base*self.height
        print("Area",area)

t1=traingle(10,20)
t1.calculate_area()

        
