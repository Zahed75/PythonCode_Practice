#pass Failed
mark=70
if mark>=30:
    print("Pass")

if mark<=30:
    print("Failed")


mark=70
if mark<=30:
    print("Pass")

else:
    print("Failed")

#largest number

num1 = 34
num2 = 43
if num1>num2:
    print(num1)

else:
    print(num2)


#check even and odd number

num = 4
if num % 2 ==0:
    print("even number")

else:
    print("odd number")


#check grades

marks=float(input("please enter your marks="))
if marks>=80:
    print("A+")
elif marks>=70:
     print("A")
     
elif marks>=60:
     print("A-")
elif marks>=50:
     print("B+")
elif marks>=40:
     print("B-")
elif marks>=30:
     print("C")
elif marks>=20:
     print("D")
else:
     print("Fail")