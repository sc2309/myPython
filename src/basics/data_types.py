x = 5   # this is an integer value
print(x)

y = "Parth"  # this is a string value or 'Parth'
print(y)

z = 3.1459   # this is a float value
print(z)

a = 4j  # this is a complex value
print(a)

b = ["pari", "parth", "dibbu", "shivay"]   #   this is a list in [] it can store different data types
print(b)
b.append("below 18")
b.insert(2, "No One")
print(b)
b.remove("No One")
print(b)
temp = [2,5,7,3,9,8,4,0,1,6] #  to delete multiple values
print(temp)
del temp[1:8]
print(temp)
temp.extend([23,56,77,88,99,20])
print(min(temp))
print(max(temp))
print(sum(temp))
temp.sort()
print(temp)

c = ("Ram Prasad", "Ahilya", "Prince", "Nikita")    #    this is a tupple in () which is same as set but immutable
print(c)

d = {"name" : "John", "age" : 36}	  #   this is a dictionary by assigning multiple values in curly braces {}
print(d)
print(d.keys())
print(d["name"])
d.get("class","not found")  #   not found will be printed as there is nothing named class
list1 = [1,2,3]
list2 = ['sarthak','rahul','shaurya']
dict1 = dict(zip(list1,list2))
print(dict1)
dict1 [4] = 'new comer'
print(dict1)
del dict1[4]
print(dict1)

e = {"apple", "banana", "cherry"}    #    this is a set in curly braces {}  the sequence in a set is not confirmed it dosen't supports index value
print(e)
#   1st parameter to start point.2nd parameter to end point.3rd point to difference
print(list(range(0,10,2)))
