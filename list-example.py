import sys
import os
import time

name = ['olarik', 'surinta']
tel = ['0954541455','0984512457']

def menu():
    os.system('clear')
    print 'Menu'
    print '======='
    print '1. Add'
    print '2. Show'
    print '3. Exit'
    
    num = int(input('Choose menu: '))
    print 'You choose number:', num
    
    if(num == 1):
        name_menu = 'add'
    elif(num == 2):
        name_menu = 'show'
    elif(num == 3):
        name_menu = 'exit'        
    else:
        name_menu = 'error'
             
    return name_menu

def show():
    os.system('clear')
    print 'Name  Tel'
    print '='*20
    for n, t in zip(name, tel):
        print n, t
        
    print 
    tmp = raw_input('Enter any key to continue ')
    if(tmp != ''):
        menu()

def add():
    print
    n = raw_input('Enter a new name: ')
    name.append(n)
    t = raw_input('Enter a telephone no.: ')
    tel.append(t)
    time.sleep(3)

def main():
    while True:
        name_menu = menu()

        if(name_menu == 'show'):
            show()
        elif(name_menu == 'add'):
            add()
        elif(name_menu == 'exit'):
            sys.exit()

if __name__ == "__main__":
    main()
