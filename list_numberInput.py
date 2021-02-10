# number=input("Enter list of numbers:")
#10 20 30 40
'''list= number.split()# 10,20,30

sum=0
for x in list:
    sum= sum+int(x)
print(sum)
'''

### List count 

CountWords=0
CountLetters=0
CountDigits=0

text=input("Please enter your values:")
# list=text.split()

for x in text:
    x=x.lower()
    if x>="a" and x<="z":
        CountLetters=CountLetters+1
    elif x>="0" and x<="9":
        CountDigits=CountDigits+1
    elif x ==" ":
        CountWords=CountWords+1

print("Numnber Of Count words:",CountWords)
print("Numnber Of Count Letters:",CountLetters)
print("Numnber Of Count Digits:",CountDigits)
