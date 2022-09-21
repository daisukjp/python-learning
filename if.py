# if

age = 20
age_alcohol = 21
if age >= age_alcohol:
    print("You can drink beer!")
else:
    print("you are too young to drink beer")

age_drive = 18

if age >= age_alcohol:
    print("you can drink beer!")
elif age < age_drive:
    print("You cannot even drive")
else:
    print("You are not allowed to drink beer but uyou can drive only if you have an license")

if not 0 < age < 120:
    print("the value is invalid")

# challenge1
balance = 1200
withdraw = 100

if balance > withdraw:
    # balance = balance - withdraw
    balance -= withdraw
    print("Your new balance is {}".format(balance))
else:
    print("you do not have money")

# challenge2
maximum = 100

if withdraw > maximum:
    print("the limit is {}" .format(maximum))
elif balance > withdraw:
    balance -= withdraw
    print("Your new balance is {}".format(balance))
