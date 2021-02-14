#xargs mane hocche function perameter same rekhe akadik value pass korano

def st_info (*details):
    print(details)
    print(details[2])
    print(details[2])

st_info(969975,"Zahed",3.76)
st_info(969976,"Zahed",3.76)
print(st_info)


#sum in x agruments

'''def jog(*summation):
    sum=0
    for num in summation:
        num=num+sum
        print(num)

jog(10,10)
jog(10,100)
jog(10,10,101)'''

def add (*summation):
    sum=0
    for num in summation:
        sum=sum+num
    print(sum)

add(10,100)
add(10,1003)
add(10,1003,220)


#xxargs hocche key dhore value pass korajar jonn 2ta** use kort hoy

# def student_info(id,name):
#     print(id,name)


# student_info(id=101,name="Zahed")

def student_info(**information):
    print(information)

student_info(id="75",name="Zahed",department="CSE")