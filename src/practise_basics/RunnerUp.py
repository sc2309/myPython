n = int(input())
lst = []
for i in range(n):
    x = int(input())
    lst.append(x)
x = max(lst)
lst.remove(x)
y = max(lst)
print(y)