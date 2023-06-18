def fib():
    print(0)
    print(1)
    a = 1
    b = 0
    for x in range(3, 13):
        c = a + b
        b = a
        a = c
        print(c)
fib()