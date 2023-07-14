from DiceSimulator import *
from randGuessing import *
def game_open():
    choise = input("Please tell which game you wanna play\nDice Simulator\nRand number guessing game\n")
    if choise == "Dice Simulator":
        RandGenerator()
    elif choise == "Rand number guessing game":
        start()