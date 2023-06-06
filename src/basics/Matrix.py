from numpy import *
x = array([
    [1, 2, 3, 7, 8],
    [4, 5, 6, 9, 0]
])
y = x.reshape(5, 2, 1)    #  (dimension, rows, amount of data)
print(y,"\n")
z = matrix('1 2 3; 4 5 6; 7 8 9')
print(z)