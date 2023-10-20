def longest_name(n, names):
    for i in range(n):
        long = max(names)
    print(long)

n = int(input())
names = []
for i in range(1,n+1):
    x = input()
    names.append(x)
longest_name(n,names)
