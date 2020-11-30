

# Inventory = {}
# daggerCount = 0
# bluepotionCount = 0
# featherCount = 0
# manuCount = 0
# playerStealth =0
# playerFlight = 0
#
# pickUp = True
#
# while True:
#
#
#     print("you are in a forest, there are four key items that you can pick up. there are daggers,blue potions, feathers "
#           "and manuscripts")
#
#     while  pickUp:
#         usr_input = input("which of these do you want to pick up:")
#         if usr_input == "daggers":
#             Inventory = ["Dagger"]
#             daggerCount +=1
#             print("you have",daggerCount ,"dagger")
#
#         elif usr_input == "blue potions":
#             Inventory = ["Blue Potions"]
#             bluepotionCount +=1
#             playerStealth +=1
#             print(Inventory)
#
#             if playerStealth == 5:
#                 print("your stealth cannot go any higher!")
#                 continue
#
#
#         elif usr_input == "feathers":
#             Inventory = ["Feathers"]
#             featherCount += 1
#             playerFlight +=1
#             print("you have", featherCount, "feather(s)")
#             print("your flight went up by" , playerFlight,"!")
#
#             if playerFlight == 5:
#                 print("your flight stat cannot go any higher!")
#
#         elif usr_input == "manuscripts":
#             Inventory = ["Manuscripts"]
#             manuCount += 1
#             print("you have", manuCount, "manuscript(s)")


# while True:
#     try:
#         a = int(input("enter a number:"))
#         b = int(input("enter another number"))
#         break
#     except ValueError:
#         print("you have to enter a number")
#
#     except ZeroDivisionError:
#         print("don't enter in zero!")
#
#     except:
#         print("something unaccepted happened!")
#
# new = int(a + b)
# print(new)


#Functions


list = []

numberCount = 0


def multiplyListByTwo():

    print(list)

multiplyListByTwo()

