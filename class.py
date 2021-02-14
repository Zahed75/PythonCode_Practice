# class is a group of information where all kind info is
#  belongs into a class and all of the elemntes are belongs to object
#class er under e sub-Class thkbe
class student():
    name=""
    gpa=""


Zara=student()
Zara.name="Zara Hasan"
Zara.gpa=3.53
print(f"Name:{Zara.name},GPA{Zara.gpa}")

#//////////////////////
Zayan=student()
Zayan.name="Zayan Hasan"
Zayan.gpa=3.53
print(f"Name:{Zayan.name},GPA{Zayan.gpa}")
# print(isinstance(rahim,student))


#Famliy in class

class family_members():
    Name=""
    B_group=""
    School=""
    contact=""
    birth_date=""
   



Zara=family_members()
Zara.Name="Zara Hasan"
Zara.B_group="B+"
Zara.School="Wills Little Flowers"
Zara.contact="0182919082"
Zara.birth_date="19january"



print(f"Name:{Zara.Name},B_group:{Zara.B_group},School:{Zara.School},Contact:{Zara.contact},birth_date:{Zara.birth_date}")

#//////////////////////////////// class er under method use kora
#Famliy in class

class family_members():
    Name=""
    B_group=""
    School=""
    contact=""
    birth_date=""
    def display(self)://--nije nijeke call korte pare
        print(f"\nName:{self.Name},B_group:{self.B_group},School:{self.School},Contact:{self.contact},birth_date:{self.birth_date}")




Zara=family_members()
Zara.Name="Zara Hasan"
Zara.B_group="B+"
Zara.School="Wills Little Flowers"
Zara.contact="0182919082"
Zara.birth_date="19january"

Zara.display()

# print(f"Name:{Zara.Name},B_group:{Zara.B_group},School:{Zara.School},Contact:{Zara.contact},birth_date:{Zara.birth_date}")
