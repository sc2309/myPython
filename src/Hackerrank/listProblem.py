if __name__ == '__main__':
    N = int(input())
    list1=[]
    for i in range(N):
        c=input().split()
        if c[0]=="insert":
            list1.insert(int(c[1]),int(c[2]))
        elif c[0]=="print":
            print(list1)
        elif c[0]=="remove":
            list1.remove(int(c[1]))
        elif c[0]=="append":
            list1.append(int(c[1]))
        elif c[0]=="sort":
            list1.sort()
        elif c[0]=="pop":
            list1.pop()
        elif c[0]=="reverse":
            list1.reverse()
