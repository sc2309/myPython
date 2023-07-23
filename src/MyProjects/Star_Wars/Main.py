import random

def Kylo_Ren():
    health = 1000
    SaberHead = 50
    saberhand = 26
    saberbody = 75
    saberleg = 20
    return health,SaberHead,saberhand,saberbody,saberleg

def Malgus():
    health = 1050
    SaberHead = 100
    saberhand = 26
    saberbody = 120
    saberleg = 20
    return health,SaberHead,saberhand,saberbody,saberleg

def Plapertine():
    health = 2000
    damage = 115
    return health,damage

def Ray():
    health = 1000
    SaberHead = 50
    saberhand = 26
    saberbody = 75
    saberleg = 20
    return health,SaberHead,saberhand,saberbody,saberleg

def luke():
    health = 1100
    SaberHead = 80
    saberhand = 26
    saberbody = 150
    saberleg = 25
    return health,SaberHead,saberhand,saberbody,saberleg

def ObiVan():
    health = 1100
    SaberHead = 75
    saberhand = 26
    saberbody = 117
    saberleg = 25
    return health,SaberHead,saberhand,saberbody,saberleg

def Yoda():
    health = 2500
    SaberHead = 100
    saberhand = 35
    saberbody = 150
    saberleg = 40
    return health,SaberHead,saberhand,saberbody,saberleg

def exit():
    print("Thanks for playing! may the force be with you.")
    start()


def P1Strike(h,sh,shand,sb,sl,h2,sh2,shand2,sb2,sl2):
    print("Select your move P1 \nlightsaber strike on head(lsh)\nlightsaber strike on hand(lshand)\nlightsaber strike on leg(lsl)\nlightsaber strike on body(lsb)\n")
    move = input()
    if move == 'lsh':
        h2 = h2 - sh2
    elif move == 'lshand':
        h2 = h2 - shand2
    elif move == 'lsl':
        h2 = h2 - sl2
    else:
        h2 = h2 - sb2
    print("P2's health is,",h2,"\n")
    if h2 == 0 or h2 < 0:
        print("P2 lost the game")
        exit()
    P2Strike(h,sh,shand,sb,sl,h2,sh2,shand2,sb2,sl2)
def P2Strike(h,sh,shand,sb,sl,h2,sh2,shand2,sb2,sl2):
    print("Select your move P2\nlightsaber strike on head(lsh)\nlightsaber strike on hand(lshand)\nlightsaber strike on leg(lsl)\nlightsaber strike on body(lsb)\n")
    move = input()
    if move == 'lsh':
        h = h - sh
    elif move == 'lshand':
        h = h - shand
    elif move == 'lsl':
        h = h - sh
    else:
        h = h - sb
    print("P1's health is,",h,"\n")
    if h == 0 or h < 0:
        print("P1 lost the game")
        exit()
    P1Strike(h,sh,shand,sb,sl,h2,sh2,shand2,sb2,sl2)

def start():
    if __name__ == '__main__':
        name = input(('Welcome to Star Jedi Fighters! Please enter a name: '))
        Player1 = input(('\n\nHere you can select a character for yourself and your opponent\n\nand your opponent will not be automatic\n\nChoose your character as P1:\n\nKylo Ren 1000\nDarth Malgus 1050\nPlapertine 2000\nRay Skywalker 1000\nLuke Skywalker 1100\nObi Van Kenobi 1100\nYoda 2500\n'))
        player2 = input('Let your opponent select his character as P2:\n\nKylo Ren 1000\nDarth Malgus 1050\nPlapertine 2000\nRay Skywalker 1000\nLuke Skywalker 1100\nObi Van Kenobi 1100\nYoda 2500\n')
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

start()