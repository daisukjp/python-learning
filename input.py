# input()

# age = input("How old are you?")
# print("your are {} years old".format(age))


# challenge1
# age = int(input("How old are yop?"))
age = 18
# age = int(age)
casino_age = 18

# if age >= 18:
#     print("You cna enter the casino")
# else: 
#     print("You can not enter this casino because your are under {}".format(casino_age))


# challenge 2

game_text = """Choice what you want to play
1: something1
2: something2
3: something3
"""

if age >= 18:
    print("You cna enter the casino")
    game = input(game_text)
    if game == '1':
        print("You selected something1")
    elif game == '2':
        print("You selected something2")
    elif game == '3':
        print("You selected something3")
    else:
        print("You have to selecte between 1 to 3")
    

else: 
    print("You can not enter this casino because your are under {}".format(casino_age))