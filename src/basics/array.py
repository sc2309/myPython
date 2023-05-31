from array import *
#   i = integer
#   u = character
#   f = float
#   d = double

x = array('i', [2,5,4,7,9])
a = array(x.typecode, (i for i in x))
print(x[4])

for y in x:
    print(y)#.reverse())

print("------------------------------------------------------")

for d in a:
    print(d)
