# Finde the largest value in three numbers

# num1=23
# num2=34
# num3=890
# if num1>num2 and num1>num3:
#     print(num1)

# elif num2>num1 and num2>num3:
#     print(num2)

# else:
#     print(num3) 


# fine the vowel and consonant

# Python Program to check character is Vowel or Consonant
# ch = input("Please Enter Your Own Character : ")

# if(ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or ch == 'A'
#        or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U'):
#     print("The Given Character ", ch, "is a Vowel")
# else:
#     print("The Given Character ", ch, "is a Consonant")


# check Grade Point

# Python Program to Calculate Grade of Student
# ----codescracker.com----

print("Enter Marks Obtained in 5 Subjects: ")
markOne = int(input())
markTwo = int(input())
markThree = int(input())
markFour = int(input())
markFive = int(input())

tot = markOne+markTwo+markThree+markFour+markFive
avg = tot/5

if avg>=91 and avg<=100:
    print("Your Grade is A1")
elif avg>=81 and avg<91:
    print("Your Grade is A2")
elif avg>=71 and avg<81:
    print("Your Grade is B1")
elif avg>=61 and avg<71:
    print("Your Grade is B2")
elif avg>=51 and avg<61:
    print("Your Grade is C1")
elif avg>=41 and avg<51:
    print("Your Grade is C2")
elif avg>=33 and avg<41:
    print("Your Grade is D")
elif avg>=21 and avg<33:
    print("Your Grade is E1")
elif avg>=0 and avg<21:
    print("Your Grade is E2")
else:
    print("Invalid Input!")