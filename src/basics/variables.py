x = 5
print(x)
y = "sarthak"    # or 'sarthak'
print(y)
z = float(3)   # we can use int(),str()  here 3 = 3.0
print(z)
a = 2
a = "changed data type"    # int to string
print(a)
b, c, d = 1, 2, 3
print(b, c, d)
e, f, g = "hello"
print(e, f, g)

m = "monday"
def localVar():
    m = 7
    print(m)
print(m)

def globalVar():
    global n
    n = 190
print(n)