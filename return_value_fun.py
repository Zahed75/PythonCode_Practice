#Sum

def add (a,b):
    sum = a+b
    return sum

result=add(10,30)
print(result)

#find the largest value using function
def largest(a,b):
    if a>b:
        return a
    elif b>a:
        return b

print(largest(100,1000))
print(largest(100,50))
print(largest(30,40))
# result=largest(20,30)
# result=largest(20,100)
# print(result)


#even odd
def even (a):
    if a%2==0:
        return "even"
    else:
        return "odd"

print(even(4))
print(even(13))

