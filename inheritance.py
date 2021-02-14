#inheritance er kaj hocche code ke re-use kora akti cls er boisishto onno cls e newa
class phone:
    def call(self):
        print("you can call")
    
    def message(self):
        print("you can message")


class realme(phone):
    # def call(self):
    #     print("you can call")
    
    # def message(self):
    #     print("you can message")
    
    def battery(self):
        print("Joldi battery palta")


p=phone()
p.call()
p.message()

print()
#///
R=realme()
R.call()
R.message()
