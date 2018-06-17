import numpy as np
import sys
import os
import time

dash_no = 30

def show_menu():
	os.system('clear')
	print "="*dash_no
	print "Shopping list menu"
	print "="*dash_no
	print "1 \t show shopping list"
	print "2 \t add shopping list"
	print "3 \t delete shopping list"
	print "4 \t EXIT"
	print "="*dash_no
	menu = input("Please Enter No. 1-4: ")
	
	return menu


def show_shopping_list(shopping_list, shopping_price, show='true'):
	os.system('clear')
	
	if(len(shopping_list)==0):
		print "="*dash_no
		print "Empty shopping list"
		print "="*dash_no
	else:	
		print "="*dash_no
		print "Shopping list \t\tPrice"
		print "="*dash_no
		for i in range(0,len(shopping_list)):
			print i+1, shopping_list[i], "\t\t", shopping_price[i]
				
		print "-"*dash_no
		print "Total \t\t\t", shopping_price.sum()
		print "="*dash_no,"\n"
	
	if(show == 'true'):
		raw_input("Press enter to continue..")


def add_shopping_list():
	os.system('clear')
	print "="*dash_no
	print "Add item to shopping list"
	print "="*dash_no
	list_s = raw_input("Input item name: ")
	list_p = input("Input item price: ")
	print "="*dash_no
	
	return list_s, list_p
	
	
def delete_shopping_list(shopping_list, shopping_price):
	os.system('clear')
	show_shopping_list(shopping_list, shopping_price, show='false')

	if(len(shopping_list) == 0):
		print "Empty shopping list!!!"
		time.sleep(3)
		show_menu()
	else:
		print "Please enter shopping list no. 1 -", shopping_price.shape[0]
		remove_list = input("Enter item number: ")
	
		if(remove_list <= shopping_price.shape[0]):
			tmp_list = shopping_list.pop(remove_list-1)
			tmp_price = shopping_price[remove_list-1]
			shopping_price = np.delete(shopping_price,(remove_list-1))
                        new_price = shopping_price
		
			print "Remove item: ", tmp_list, tmp_price, "\n"
			show_shopping_list(shopping_list, shopping_price, show='false')
			time.sleep(1)
		else:
			print "Number out of range"
	return new_price

# start program
def main():
	shopping_list = ['pen']
	shopping_price = np.array([20])
	#shopping_list = []
	#shopping_price = np.array([])
	
	while True:
		menu = show_menu()

		if(menu == 1):		
			show_shopping_list(shopping_list, shopping_price)
		elif(menu == 2):
			s, p = add_shopping_list()		
			shopping_list.append(s)
			shopping_price = np.hstack((shopping_price,p))	
	
			print "Added item completed"
			show_shopping_list(shopping_list, shopping_price, show='false')
			time.sleep(1)
		elif(menu == 3):
			shopping_price = delete_shopping_list(shopping_list, shopping_price)

		if(menu == 4):
			os.system('clear')
			print "Exit Shopping List"
			print "Thank you!!!"
			sys.exit()


if __name__ == "__main__":
	main()	
