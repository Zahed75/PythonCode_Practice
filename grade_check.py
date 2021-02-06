#grade check in logical operator

print("Please enter your 5 sub marks:")
sub1=float(input())
sub2=float(input())
sub3=float(input())
sub4=float(input())
sub5=float(input())
marks=sub1+sub2+sub3+sub4+sub5
mark=marks/5
if mark>=80 and mark<=100:
    print("A+")

elif mark>=70 and mark<80:
    print("A-")

elif mark>=60 and mark<70:
    print("B")

else:
    print("Fail")