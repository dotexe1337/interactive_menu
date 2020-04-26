#!/usr/bin/env python
# -*- coding: utf-8 -*-

# first we will set our variables
restaurant_name = "Simple Restaurant" # set our restaurant name
subtotal = 0 # subtotal (starts at 0)
tax_rate = 0.07 # tax rate

menu = [("Nothing", 0), ("Sandwich", 5), ("Salad", 7.5), ("Fries", 3), ("Apple", .75), ("Soda", 1.5), ("Milk", 1)]# the menu variable is a list of tuples made up of strings for the names of food and drink items followed by their prices. the prices are in USD and can be either an integer or a floating point number.

# let's start our menu
print("Welcome to {0}!\n".format(restaurant_name), "Heres's the menu:") # print a welcome message
for i in menu: print("{0}. {1:.<20} ${2:.2f}".format(menu.index(i), i[0], i[1])) # print all of the items in our menu with fancy formatting

# let's start our user input handling
while True: # infinite while loop (True is always True, of course)
	print("Type a menu item number, and then press ENTER.\nType 0 when you're done:") # print some text to tell the user to type an item number and press 0 if done
	try: # we'll start a try/catch (try/except in python) statement
		item_number = int(input()) # item number is an integer assigned to user input
		if item_number == 0: break # if item number is 0 then break the while loop
		elif item_number < len(menu) and item_number > 0:  # else if item number is smaller than the length of the menu tuple and bigger than 0
			subtotal += menu[item_number][1] # add the price of the item to the subtotal
			print("Your current total is ${0:.2f}.".format(subtotal)) # print some text to let the user know what's going on
		else: print("That item doesn't exist on the menu!") # if the item number (user's input) doesn't match our previous constraints, then tell the user that item doesnt exist
	except SyntaxError: # if there is a syntax error (user doesn't type any input)
		print("You didn't type an item number.") # tell the user that they didn't type an item number

# finally, let's calculate the prices and let the user finish ordering.
if subtotal == 0: # if subtotal is 0
	print("Not hungry?") # i guess you're not hungry
else: # if subtotal is not not 0 (makes sense?)
	tax = subtotal * tax_rate # calculate tax
	tip_rate = 0 # make an initial tip rate variable (starting value of 0)
	tip = 0 # make an initial tip variable (starting value of 0)
	while True: # infinite while loop
		try: # start a try/catch (try/except in python) statement
			print("Please type a tip rate (in percentage).") # print some text to let the user know they need to type a tip rate
			tip_rate = int(input()) # assign an integer of user input to tip_rate	
			tip_rate = tip_rate * 0.01 # convert the tip_rate to a decimal place
			tip = subtotal * tip_rate # calculate tip
			break # break the infinite while loop
		except SyntaxError: # if there's a syntax error (user doesn't type any tip rate)
			print("You didn't type a tip rate.") # tell the user they didn't type a tip rate
	total = subtotal + tax + tip # calculate subtotal
	print("\nHere's your bill:") # print text to let the user know what's going on
	print("Subtotal: ${0:.2f}".format(subtotal)) # print the subtotal
	print("{rate:.0%} tax: ${amount:.2f}".format(rate=tax_rate, amount=tax)) # print the tax rate and total amount of tax
	print("{rate:.0%} tip: ${amount:.2f}".format(rate=tip_rate, amount=tip))
	print("Total: ${0:.2f}\n".format(total)) # print total
	print("Thank you. Please come again!") # thank the user
