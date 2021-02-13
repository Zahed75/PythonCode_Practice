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

result=largest(20,30)
result=largest(20,100)
print(result)
