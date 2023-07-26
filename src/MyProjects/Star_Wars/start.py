import random
from strike import *
from Characters import *

def Start():
        name = input('Welcome to Star Jedi Fighters! Please enter a name: ')
        print('\nYour opponent will not be automatic\n\nChoose your character as P1\nsometimes a character may undergo aggeression and may\ncause mor damage than normal\n')
        Player1 = input('\n\nHere you can select a character for yourself\n\nKylo Ren 500\nDarth Malgus 550\nPlapertine 700\nRay Skywalker 500\nLuke Skywalker 650\nObi Van Kenobi 650\nYoda 1000\n')
        player2 = input('Let your opponent select his character as P2:\n\nKylo Ren 500\nDarth Malgus 550\nPlapertine 700\nRay Skywalker 500\nLuke Skywalker 650\nObi Van Kenobi 650\nYoda 1000\n')
        if Player1 == 'Kylo Ren':
            h,sh,shand,sb,sl = Kylo_Ren()
        elif Player1 == 'Darth Malgus':
            h,sh,shand,sb,sl = Malgus()
        elif Player1 == 'Plapertine':
            h,sh,shand,sb,sl = Plapertine()
        elif Player1 == 'Ray Skywalker':
            h,sh,shand,sb,sl = Ray()
        elif Player1 == 'Luke Skywalker':
            h,sh,shand,sb,sl = luke()
        elif Player1 == 'Obi Van Kenobi':
            h,sh,shand,sb,sl = ObiVan()
        else:
            h,sh,shand,sb,sl = Yoda()

        if player2 == 'Kylo Ren':
            h2,sh2,shand2,sb2,sl2 = Kylo_Ren()
        elif player2 == 'Darth Malgus':
            h2,sh2,shand2,sb2,sl2 = Malgus()
        elif player2 == 'Plapertine':
            h2,sh2,shand2,sb2,sl2 = Plapertine()
        elif player2 == 'Ray Skywalker':
            h2,sh2,shand2,sb2,sl2 = Ray()
        elif player2 == 'Luke Skywalker':
            h2,sh2,shand2,sb2,sl2 = luke()
        elif player2 == 'Obi Van Kenobi':
            h2,sh2,shand2,sb2,sl2 = ObiVan()
        else:
            h2,sh2,shand2,sb2,sl2 = Yoda()

        x = random.randrange(1, 3)
        if x == 1:
            print("Player 1 got first chance\n\n")
            P1Strike(h,sh,shand,sb,sl,h2,sh2,shand2,sb2,sl2)
        else:
            print("Player 2 got first chance\n\n")
            P2Strike(h,sh,shand,sb,sl,h2,sh2,shand2,sb2,sl2)