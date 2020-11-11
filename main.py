#program to check if a number is even or odd

user_input = int(input("type in any number")) #The user inputs a number and the program decided if it is even or odd

odd_or_even = (user_input + 2) / 2

if odd_or_even == int(odd_or_even):
    print("this number is even")
elif odd_or_even == float(odd_or_even):
    print("this number is odd")


#program to check the contents of a string

word = str(input("enter in a word"))

if len(word) == 3:
    print(word + "ing")
elif "ing" in word:
    print(word + "ly")
else:
    print(word + "ly")


#text based adventure

player_input = input("""Welcome! It seems that you are lost in this forest, 
so I will be your guide to leave!
(press the A key to continue)""")

if player_input == "A" or player_input == "a":
    player_input = input("We have arrived at a crossroad, which way should we go? (Left/Right)")

    if player_input == "left":
        player_input =input("""Some fallen trees are blocking our path. 
        Should we start a fire and burn them? or should we find another way? 
        (burn/other )""")

        if player_input == "burn":
            player_input =input(""""The trees are now burned. Uh oh! A forest fire is starting! Should we run away or find some water to put "
                                 out the forest fire? (run/water)""")

            if player_input == "water":
                print("You couldn't find any water in time to put out the forest fire, you were burnt to a crisp. GAME OVER!")

            elif player_input == "run":
                print("Due to the fire burning the entire forest down, you were able to easily find your way out. YOU WIN!")

        elif player_input == "other":
            print("after walking through a different section of the forest, you eventually found the exit, YOU WIN!")

        else:
            print("invalid input!")

    elif player_input == "right":

        player_input = input("Oh! It's starting to rain, let's look for cover (press A to continue)")

        if player_input == "A" or player_input == "a":
            player_input =input("We can stay in this cave until the rain has stopped. Do you want to sleep?(yes/no)")

            if player_input == "yes":
                print("You were murdered while asleep. GAME OVER!")

            elif player_input == "no":
                    player_input =input("""You stayed up the entire night. Good morning! let's continue on our way out of here 
                    (press A to continue)""")

                    if player_input == "a" or player_input == "A":
                        print("Oh look! there's the the exit! YOU WIN!")

                    else:
                        print("invalid input!")

            else:
                print("invalid input!")

        else:
            print("invalid input!")
    else:
         print("invalid input")
else:
    print("invalid input")

















