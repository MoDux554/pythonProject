# position = 5 #this is an interger
moving_step = 0.2 #this is a float
# this_word = "hello world" #this is a string, it can be in either singular or double quotation marks
#
# number_1 = 4
# number_2 = 4
#
#
# position +=1 #the current value of "position" will increase by 1 in increments
# position -=1 #the current value of "position" will decrease by 1 in increments
#
# name = "Mo"
# phrase = 'that\s fine' #helps when using single quotes and aphrostrophes
#
# Name_two = "monolith"
#
# print("my position is %d, my moving step is %.2f, my name is %s" %(position,moving_step,name))
# print("my position is {2}, my moving step is {0}, my name is {1}".format(position,moving_step,name) )
#
# print(name[0]) #outputs the first letter of the string assigned to that variable
# print(name[-1]) #outputs the last letter of the string assigned to that variable]
# print(Name_two[-3])



#
# promt = input("give me a number")
# inter = int(promt)
#
# print(inter + 7)

# gameOn = False
#
# if gameOn:
#     print("this is true")
# elif moving_step ==0.2:
#     print("yes")
# else:
#     print("this is false")


number_lower = 100
number_upper = 1000

user_input = input("please enter any number")

int_version = int(user_input)
if int_version <= number_lower:
    print("that is a small number!")
elif int_version>=number_lower and int_version <= number_upper:
    print("that is not a big number yet!")
else:
    print("that is an adequetely huge number!")