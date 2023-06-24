from functools import reduce

lis = []
for x in range(10):
    a = int(input())
    lis.append(a)
l1 = list(filter(lambda i : i%5==0,lis))
print(l1)
l2 = list(map(lambda n : n - 1,l1))
print(l2)
l3 = reduce(lambda j,k : j+k,l2)
print(l3)
