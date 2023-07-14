import random

def start():
    def intro():
        print("Hello user Lets see if you can guess the right number between 0 to 3\nYou have 3 lives and we will give you 2 hint\n")


    def inputF():
        guess = int(input())
        return guess


    def randGen():
        rand = random.randrange(3)
        return rand


    def checkFunc(guess):
        temp = randGen()
        print(temp)
        for i in range(6):
            if guess == temp:
                print("you win :)")
                intro()
            elif guess < temp:
                print("You guess is smaller than answer you lose :|")
            else:
                print("Your guess is greater than answer you lose :|")

    intro()
    guess = inputF()
    checkFunc(guess)
