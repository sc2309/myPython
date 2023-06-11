import random


def RandGenerator():
    x = random.randrange(1, 7)
    return x


r = RandGenerator()
x = input("Press S and then enter to start: ")
print("------------")
print("|          |")
print("|    {}     |".format(r))
print("|          |")
print("------------")
