def func(lis):
    count = 0
    for i in range(10):
        if len(lis[i]) > 5:
            count += 1
    return count
lst = []
for i in range(10):
    z = input()
    lst.append(z)
c = func(lst)
print(c)
