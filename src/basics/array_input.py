from array import *
arr = array('i', [])
x = int(input("hello please enter array length: "))
for i in range(x):
    y = int(input("enter a number:"))
    arr.append(y)
print("--------------------------------------------------")
for i in range(x):
    print(arr[i])

r = int(input("Enter the value to find:"))
k = 0
for c in range(x):
    if r == arr[c]:
        print("At index value {}".format(k))
    k += 1
