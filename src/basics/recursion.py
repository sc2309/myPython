import sys
sys.setrecursionlimit(10000)
print(sys.getrecursionlimit())

def recur(n):
    if n == 1:
        return 1
    return n + recur(n - 1)
n = int(input("Please enter the limit: "))
res = recur(n)
print(res)
