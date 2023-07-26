

def exit():
    print("Thanks for playing! may the force be with you.")

def P1Strike(h,sh,shand,sb,sl,h2,sh2,shand2,sb2,sl2):
    print("Select your move P1 \nlightsaber strike on head(lsh)\nlightsaber strike on hand(lshand)\nlightsaber strike on leg(lsl)\nlightsaber strike on body(lsb)\n")
    move = input()
    if move == 'lsh':
        h2 = h2 - sh2
    elif move == 'lshand':
        h2 = h2 - shand2
    elif move == 'lsl':
        h2 = h2 - sl2
    elif move == 'lsb':
        h2 = h2 - sb2
    else:
        print('missed')
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
    elif move == 'lsb':
        h = h - sb
    else:
        print('missed')
    print("P1's health is,",h,"\n")
    if h == 0 or h < 0:
        print("P1 lost the game")
        exit()
    P1Strike(h,sh,shand,sb,sl,h2,sh2,shand2,sb2,sl2)