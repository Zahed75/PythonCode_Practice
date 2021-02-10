#1+2+3+4+5+.......n

'''number=int(input("Enter your last number:"))
sum = 0
for x in range(1,number+1,1):
    sum = sum+x

print(sum)

'''
#------2+4+6+8+10---------n
'''num=int(input("Enter your last number:"))

jogfol= 0

for x in range(2,num+1,2):
    jogfol=jogfol+x

print(jogfol)'''

#------print 1+3+5+7+++++n

'''num=int(input("Enter your last number:"))

jogfol= 0

for x in range(1,num+1,2):
    jogfol=jogfol+x

print(jogfol)'''

#print 4+8+16+32+64----+n


'''num=int(input("Enter your last number:"))

jogfol= 0

for x in range(4,num+1,4):
    jogfol=jogfol+x

print(jogfol)
'''

#Series of power
#--1^1+2^2+3^3+4^4----+n^n

'''num=int(input("Please enter your last number:"))

sum = 0
for x in range(1,num+1,1):
    sum=sum+x*x

print(sum)'''

#------1 + ½ + 1/3 + …. + 1/n------
'''1 k 1 theke 10 porjnto vag kore vagfol gula jog krtse'''
#https://www.youtube.com/watch?v=VzOhGRsRKM4
n=int(input("Enter the number of terms: "))
sum1=0
for i in range(1,n+1):
    sum1=sum1+(1/i)
print(sum1)

