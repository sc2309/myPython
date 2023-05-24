x = int(input("Enter any number: "))
if x <= 10:
    print("small than 10 oe equal to 10")
    if x <= 5:
        print("smaller than equal to 5")
elif x <= 50 and x >= 11:
    print("smaller than equal to 50")
elif x <= 75 and x >= 51:
    print("smaller than equal to 75")
else:
    print("greater than 75")