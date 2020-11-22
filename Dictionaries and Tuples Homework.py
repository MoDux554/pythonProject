#Exercise 1: Write a Python script to print a dictionary where the
#keys are numbers between 1 and 20 (both included) and the
#values are the square of their keys.

# n = dict()
#
# for x in range(0,21):
#     n[x] = x**2
# print(n)


#Exercise 2: The following Dictionary includes some duplicate value
#entries (item1 and item3). Write a program to remove them.

# room_items = {"item1" : {"Name" : "Lamp" , "Colour" : "Red" }, "item2" : {"Name" : "Table" , "Colour" :"Brown ", "Type" :0} , "item3": {"Name" : "Lamp" , "Colour" : "Red"}, "itme4" : {"Name" : "Chair" , "Colour" : "Green" , "Type" : 0}}
#
# # del room_items["item1"]
# # del room_items ["item3"]
# # print(room_items)


# Exercise 3: Write a program that uses a dictionary to store a
# number of items in an inventory for an adventure game. The player
# should be able to pick new items for the inventory and use items
# from the inventory. Using an item may affect variables such as
# ‘health’, ‘magic’ or ‘courage’. You may want to use a dictionary to
# store these too. Be sure to check for the correct user input.




#Exercise 3

# player_inventory = {}
#
# usr_input = input("You have found a stick on the ground. \n"
#                   "pick it up?")
#
# if usr_input == "yes":
#     player_inventory["Weapon"] = "stick"
#     player_inventory["Damage"] = "5"
#     print("the stick has been added to the inventory")
#     print(player_inventory)
#
# elif usr_input == "no":
#     print("you continue walking")