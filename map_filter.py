
#map function has a two part one is function and another is iteratble
# def square(x):
#     return x*x

# num=[10,3,2,23,42,32,23]

# result=list(map(square,num))
# print(result)

def even(num):
    print(num)
    if num%2==0:
        return num
    else:
        return "not even"

    
        
num=[10,3,2,23,42,32,23]
result=list(map(even,num))
print(result)
