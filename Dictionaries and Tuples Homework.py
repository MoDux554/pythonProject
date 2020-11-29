#Exercise 1: Write a Python script to print a dictionary where the
#keys are numbers between 1 and 20 (both included) and the
#values are the square of their keys.

# n = dict()
#
# for x in range(1,21):
#     n[x] = x**2
# print(n)


#Exercise 2: The following Dictionary includes some duplicate value
#entries (item1 and item3). Write a program to remove them.

#check for duplicates then remove them



# room_items = {"item1" : {"Name" : "Lamp" , "Colour" : "Red" }, "item2" : {"Name" : "Table" , "Colour" :"Brown ", "Type" :0} , "item3": {"Name" : "Lamp" , "Colour" : "Red"}, "item4" : {"Name" : "Chair" , "Colour" : "Green" , "Type" : 0}}
# room_items_2 ={}
#
# for k,v in room_items.items():    #iterates through room_items
#     if v not in room_items_2.values():   #checks if there are values not already in room_items_2
#         room_items_2[k] = v     #assigns that value to the key in room_items_2
# print(room_items_2)




#Exercise 3

#try adding in more than one weapon, and the player can choose which of those weapons to use in a fight
#try using a for and while  loop to run through the dictionary containing weapons so that when a player inputs a weapon they don't have
#the program returns a statement saying "input invalid" and they are able to input again

player_inventory = {}
playerHealth = 15

stickDamage = 5

enemy01Attack = 3
enemy01Health = 10

nextEnemy = 0




# Scenario = "start"
#
#
#
# while True:
#
#     if Scenario == "start":
#         usr_input = input("You have found a stick on the ground. \n"
#                           "pick it up?")
#         if usr_input == "yes":
#             player_inventory["Stick"] = 5
#             print("the stick has been added to the inventory")
#             print(player_inventory)
#             usr_input = input("press A to continue")
#             if usr_input == "a":
#                 Scenario = "Battle01"
#
#
#
#
#         if  usr_input == "no":
#             print("you continue walking")
#             Scenario = "Battle01"
#
#
#     elif  Scenario == "Battle01":
#         print("A monster stands in your path!")
#         if enemy01Health:
#             if player_inventory == {}:
#                 print("You have nothing to protect yourself with, you were mauled to shreds!")
#                 break
#             else:
#                 print("What do you want to do?")
#                 if enemy01Health > 0:
#                     usr_input = str(input("Enter in either Fight or Run:"))
#                     if usr_input == "Fight":
#                         print(player_inventory)
#                         usr_input = str(input("Choose your weapon:"))
#                         if usr_input == "Stick":
#                             enemy01Health -= player_inventory["Stick"]
#                             print("the enemy's health is", enemy01Health, "HP")
#                     elif usr_input == "Run":
#                         print("You ran away succesfully!")
#                         Scenario = "Hub01"
#         elif enemy01Health == 0:
#           nextEnemy += 1
#           print("You win!")
#           usr_input = input("Press A :")
#           if usr_input == "a":
#               Scenario = "Hub01"
#
#
#
#
#     elif Scenario == "Hub01":
#         print("What do you want to do?")
#         usr_input = str(input("enter either Walk or Bag"))
#         if usr_input == "Walk":
#
#             usr_input = input("A rock is lying on the ground. Pick it up? (yes/no)")
#             if usr_input == "yes":
#
#                 player_inventory["Rock"] = 10
#                 print("The Rock was added to your inventory")
#                 print(player_inventory)
#
#             elif usr_input == "no":
#
#                 print("You continued walking")
#                 Scenario = "Battle01"
#
#         elif usr_input == "Bag":
#             print("What do you want to check? (Weapons/Items")
#             usr_input = input(":")
#             if usr_input == "Weapons":
#                 print(player_inventory)
#             elif usr_input == "Items":
#                 print("There is nothing here")



#textAdventFile exercise

# weapons = ["sword", "dagger"]
# fightMode = False
#
# while True:
#
#     usr = input("Where to? ")
#
#     if usr in ["n", "north", "west", "w", "east", "e", "south", "s"]:
#         print("Oh this looks like trouble!")
#
#         usr = input("Will you fight?").lower()
#         if usr in ["yes", "y", "hell yeah"]:
#             fightMode = True
#
#         if fightMode:
#             usr = input("which weapon you want to use: ")
#
#             usr_words = usr.split(" ")  # list
#
#             for word in usr_words:
#                 if word in weapons:
#                     if word == "sword":
#                         print("With this you do 5 damage. On we go!")
#                     elif word == "dagger":
#                         print("With this you do 3 damage. On we go!")
#                 else:
#                     print("please choose a weapon you actually have")
#
#
#     # Further code for the fight ...
#     else:
#         print("try again")







