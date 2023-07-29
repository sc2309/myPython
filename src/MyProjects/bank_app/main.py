from menu import *

if __name__ == '__main__':
    count = 3
    for x in range(1, 4):
        app_pass = input('Enter the correct password: ')
        set_pass = '149826'
        count -= 1
        if app_pass == set_pass:
            print('Hello user,You can')
            menuItems()
        else:
            print('Wrong Password!', count, 'tries left')
        if count == 0:
            break
