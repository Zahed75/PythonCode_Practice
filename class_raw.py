# class student():
#     name=""
#     roll=""

#     def value_pass(self,name,roll):#akhne value pass korarnor akti function use kora hoyeche
#         self.name=name
#         self.roll=roll

# #akhane self akta convention keyword jar kaj hocche elemnet value nije nije call dibe
#     def show(self):
#         print(f"Name:{self.name},Roll:{self.roll}")


# Zahed=student()
# # Zahed.name="Zahed Hasan"
# # Zahed.roll=244
# Zahed.value_pass("Zahed",75)
# Zahed.show()

#Construcutor

class family():
    name=""
    blood_group=""

    def __init__(self, name, blood_group):
       self.name=name
       self.blood_group=blood_group
    
    def show(self):
        print(f"Name:{self.name},Roll{self.blood_group}")


Zayan=family("Zahed","B+")

Zayan.show()