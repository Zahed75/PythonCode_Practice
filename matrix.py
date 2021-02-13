matrix=[
    [1,2,3],#1 no row/colum index 0 theke start hobe
    [2,4,5], #2no Row/colum index 0 theke start hobe
]
print(matrix[1][2])

#change the matrix value change

'''matrix[1][2]=10
print(matrix[1][2])'''

#print coloum wise matrix value

for row in matrix:
    for column in row:
        print(column)
