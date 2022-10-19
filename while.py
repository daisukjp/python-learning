# while loop# while loop
count = 0
while count < 10:
    print(count)
    count += 1

# break & continue

# while True:
#     age = int(input("How old are you?"))
#     if not 0 <= age < 120:
#         print("invalid number")
#         continue
#     else:
#         print(f"You are {age} years old")
#         break

# challenge
age = int(input("How old are you?"))
casino_age = 18

game_text = """Choice what you want to play
1: something1
2: something2
3: something3
"""

if age >= 18:
    print("You cna enter the casino")
    while True:
        game = input(game_text)
        if game == '1':
            print("You selected something1")
            break
        elif game == '2':
            print("You selected something2")
            break
        elif game == '3':
            print("You selected something3")
            break
        else:
            print("You have to selected between 1 to 3")
            continue
else:
    print("You can not enter this casino")