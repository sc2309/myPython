#       accessing a character in a string 
a = 'i like coding'
print(a[0], "\n")

#       accessing every character in a string
for x in a:
    print(x)

#   length of a string  imp

print(len(a))

#   checking a word or a character in a string

print('coding' in a)

#   checking a word or a character in a string using if else and not in

if 'worse' not in a:
    print('good statement')

#    slicing technique

print(a[7:13])
print(a[-13:-7])

#   string with upper and lower case and replace and split. strip() is used to remove space from end or start
print(a.upper())
print(a.lower())
b = "I like / Resting Also"
print(b.split(" / "))

print(a.replace('c', 'C'))
