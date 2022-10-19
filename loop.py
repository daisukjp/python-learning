# loop else

# for else
# fruits = ['apple', 'peach', 'grapes', 'banana']
#
# for fruit in fruits:
#     choice = input(f"Are you looking for {fruit}? y/n:")
#     if choice == "y":
#         print("Nice")
#         break
#     else:
#         print("Oh, got it")
# else:
#     print("loop has finished")

# while

# count = 0
# while count < 0:
#     print(count)
#     count += 1
# else:
#     print("count is no longer less than 10")

# ex
balance = 1000
game_price = 200

while balance >= game_price:
    choice = input(f"Do you want to spend {game_price}yen for game? (balance:{balance}yen)(y/n?):")
    if choice == "y":
        balance -= game_price
        print(balance)
    elif choice == "n":
        print("Let's play again")
        break
    else:
        print("y or n")
else:
    print(f"You have {balance}yen, you cannot play this anymore")
