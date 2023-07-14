import random


def RandGenerator():
    x = random.randrange(1, 7)        #   function generates random numbers
    # x = input("Press S and then enter to start: ")
    c = 0
    #  starts printing a dice structure
    print("------------")
    for j in range(2):
        print("|          |")
        if c == 0:
            print("|    {}     |".format(r)) #  prints the line in which the number will be written
        c += 1

    print("------------")