# Finde the largest value in three numbers

num1=23
num2=34
num3=890
if num1>num2 and num1>num3:
    print(num1)

elif num2>num1 and num2>num3:
    print(num2)

else:
    print(num3) 


# fine the vowel and consonant

# Python Program to check character is Vowel or Consonant
ch = input("Please Enter Your Own Character : ")

if(ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or ch == 'A'
       or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U'):
    print("The Given Character ", ch, "is a Vowel")
else:
    print("The Given Character ", ch, "is a Consonant")