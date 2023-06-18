import random


def intro():
    print("Hello user Lets see if you can guess the right number between 0 to 10\nYou have 3 lives and we will give you 2 hint\n")


def inputF():
    guess = int(input())
    return guess

lives = 4


def randGen():
    rand = random.randrange(50)
    return rand


def checkFunc(guess,lives):
    temp = randGen()
    print(temp)
    for i in range(6):
        if guess == temp:
            print("you win :)")
            intro()
        elif guess < temp:
            print("You guess is smaller than answer :|")
            lives -= 1
            print("                                                                                      LIVES: ",lives)
        else:
            print("Your guess is greater than answer :|")
            lives -= 1
            print("                                                                                      LIVES: ",lives)
        if lives == 0:
            print("You lose :(")
            break
        inputF()

intro()
guess = inputF()
checkFunc(guess, lives)
