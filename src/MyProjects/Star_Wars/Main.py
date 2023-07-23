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
    saberbody = 125
    saberleg = 20
    return health,SaberHead,saberhand,saberbody,saberleg

def Plapertine():
    health = 2000
    damage = 100
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
    SaberHead = 50
    saberhand = 26
    saberbody = 100
    saberleg = 20
    return health,SaberHead,saberhand,saberbody,saberleg

def ObiVan():
    health = 1100
    SaberHead = 50
    saberhand = 26
    saberbody = 75
    saberleg = 20
    return health,SaberHead,saberhand,saberbody,saberleg

def Yoda():
    health = 2500
    SaberHead = 100
    saberhand = 35
    saberbody = 150
    saberleg = 40
    return health,SaberHead,saberhand,saberbody,saberleg

def P1Strike(count,h,sh,shand,sb,sl,h2,sh2,shand2,sb2,sl2):
    for i in range(10000):
        print("Select your move\nlightsaber strike on head\nlightsaber strike on hand\nlightsaber strike on leg\nlightsaber strike on body\n")
        move = input()
    count = 1
    if move == 'lightsaber strike on head':
        h2 = h2 - sh
    elif move == 'lightsaber strike on hand':
        h2 = h2 - shand
    elif move == 'lightsaber strike on leg':
        h2 = h2 - sl
    else:
        h2 = h2 - sb
    if count == 1:
        P2Strike(count)
def P2Strike(count,h,sh,shand,sb,sl,h2,sh2,shand2,sb2,sl2):
    pass

if __name__ == '__main__':
    count = 1
    name = input(('Welcome to Star Jedi Fighters! Please enter a name: '))
    Player1 = input(('\n\nHere you can select a character for yourself and your opponent\n\nand your opponent will not be automatic\n\nChoose your character as:\n\nKylo Ren 1000\nDarth Malgus 1050\nPlapertine 2000\nRay Skywalker 1000\nLuke Skywalker 1100\nObi Van Kenobi 1100\nYoda 2500\n'))
    player2 = input('Let your opponent select his character:\n\nKylo Ren 1000\nDarth Malgus 1050\nPlapertine 2000\nRay Skywalker 1000\nLuke Skywalker 1100\nObi Van Kenobi 1100\nYoda 2500\n')
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
        P1Strike(count,h,sh,shand,sb,sl,h2,sh2,shand2,sb2,sl2)
    else:
        print("Player 2 got first chance\n\n")
        P2Strike(count,h,sh,shand,sb,sl,h2,sh2,shand2,sb2,sl2)