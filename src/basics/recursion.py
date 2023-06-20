import sys
sys.setrecursionlimit(10000)
print(sys.getrecursionlimit())
i = 0
def show():
    print("please enter the number till which you have to count: ")

def recur():
    global i
    print(i)
    i += 1
    if i == 10:
        show()
    recur()
show()
n = int(input())
recur()
