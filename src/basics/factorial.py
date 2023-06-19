def fact(n):
    k = 1
    for x in range(1, n + 1):
        k = k * x
    print(k)


n = int(input())
fact(n)