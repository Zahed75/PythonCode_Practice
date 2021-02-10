#pattern joto row hobe toto liner er variable maan dite hobe
'''
*
**
***
****
*****'''
'''n=5
for x in range(n+1):
    print(x*"*")

'''
#--------------
'''
*   (2*i-1)
***
*****
*******
*********
'''

'''
n=5

for x in range(n+1):
    print((2*x-1)*"*")

'''

''' 
 *
 **
 ***
 ****
 *****
 ******'''


'''
n=6
for x in range(1,n+1):
     for j in range(1,x+1):
         print("*",end="")
     print("\n")
'''


#space pattern

for x in range(1,6):
    for y in range(1,6-x):
        print(" ",end="")
    for z in range(1,x+1):
        print("*",end="")
    print("\n")
   


