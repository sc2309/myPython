def menuItems():
    mainInput = input('transfer money\npay bills\nDATA recharge\nmovie tickets\ntravel tickets\n')
    if mainInput == 'transfer money':
        pass
    elif mainInput == 'pay bills':
        bills()
    elif mainInput == 'DATA recharge':
        DATA()
    elif mainInput == 'movie tickets':
        pass
    elif mainInput == 'travel tickets':
        pass
    else:
        gotomenu()

def bills():
    billInput = input('Please enter which bill you want to pay\nelectricity\nwater\nLPG')
    if billInput == 'electricity':
        pass
    elif billInput == 'water':
        pass
    elif billInput == 'LPG':
        pass
    else:
        gotomenu()

def DATA():
    DATAInput = input('Please enter what you want to recharge\nWi-Fi\nmobile calls only\nmobile everything')
    if DATAInput == 'Wi-Fi':
        pass
    elif DATAInput == 'mobile calls only':
        pass
    elif DATAInput == 'mobile everything recharge':
        pass

def gotomenu():
    print('Not an option from menu')
    menuItems()
