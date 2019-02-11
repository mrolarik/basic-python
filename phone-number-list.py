#python version 3

import sys
import os
import time

name = ['car','faik','marco']
tel = ['045xxxx','095xxxx','083xxxx']

def menu():
    while (True):
        print('contact list')
        print('-'*15)
        print('1. show')
        print('2. search')
        print('3. add')
        print('4. delete')
        print('0. exit')
        print('-'*15)

        menu_no = input('select no. 0 to 4:')

        if (menu_no.isdigit()):
            print('correct input')

            if (int(menu_no) == 0):
                sys.exit()
            elif(int(menu_no) == 1):
                os.system('cls')
                show()
            elif(int(menu_no) == 2):
                os.system('cls')
                search()
            elif(int(menu_no) == 3):
                os.system('cls')
                add()
            elif(int(menu_no) == 4):
                os.system('cls')
                delete()
            else:
                os.system('cls')
                print('inconrrect input')
        else:
            os.system('cls')
            print('input inconrrect')


def show():
    print('Phone Number')
    print('='*20)
    for idx, na in enumerate(name):
        print("no.",idx+1, "\t name:", na, "\t tel:",tel[idx])
    print()


def search():
    search_name = input('Search from name: ')
    search_name = search_name.lower()

    if(search_name in name):
        idx = name.index(search_name)
        #print(search_name, 'is in contact list')
        #print('name:', name[idx], 'tel:', tel[idx])
        print('name:', search_name, 'tel:', tel[idx])
    else:
        print('not found')


def add():
    print('Add new contact list')
    print('='*20)
    input_name = input('Name: ')
    input_tel = input('Telephone No.: ')

    name.append(input_name)
    tel.append(input_tel)

    print('Added Success!!')
    time.sleep(2)


def delete():
    print('Delete contact from contact list')
    print('='*20)

    print('\n')
    input_name = input('Input name you want to delete: ')
    input_name = input_name.lower()

    if(input_name in name):
        idx = name.index(input_name)
        print("name: %s \t number: %s " %(name[idx], number[idx]))
        print('\n')
        confirm_key = raw_input('Do you want to delete (y/n)? ')
        if(confirm_key.lower() == 'y'):
            name.pop(idx)
            tel.pop(idx)
            print('Delete Success!!')
            time.sleep(2)
    else:
        print('Name Not found!!!')



def main(): #definition
    menu()

if __name__=='__main__':
    main()
