#File open read write operation
file=open("student_info.txt","r+") #r+ mane hocche read and write dui ta e access dewa
# print(file.readable())
# text=file.read()
# print(text)
# size=len(text) #len diye file size ber korar jonno
# print(size)
# text=file.readlines()[0:3]
# print(text)

#file access in for loop

for x in file:
    print(x)
file.close()