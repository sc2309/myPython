a = "Python is easy"

#     text align center
print(a.center(140, " "))

#    counting how many number of times a specific value occurs string.count(value, start, end)
x = a.count("s")
print(x)

#   return if the specific string ends with specific character string.endswith(value, start, end)
b = a.endswith("y")
print(b)

#   set tab size NOTE:- Default tabsize is 8
txt = "H\te\tl\tl\to"

x = txt.expandtabs(2)

print(x)
