# for loop

# fruits = ['apple', 'peach', 'melon', 'grapes']

# for fruit in fruits:
#     print(f"I love {fruit}!!")

# for char in "Hello World!!":
#     print(f"char: {char}")

# # challenge1 

# user_input = input("What kind of fruit do you love?")

# for fruit in fruits:
#     if fruit == user_input:
#         print("I love {}!!".format(fruit))

# challenge2
user_favorite = []
normal = []
fruits = ['apple', 'peach', 'melon', 'grapes']
for fruit in fruits:
    choice = input(f"Do you like {fruit}? y/n")

    if choice == 'y':
        user_favorite.append(fruit)
    else: 
        normal.append(fruit)

print(f"favorite fruits: {user_favorite}")
print(f"normal fruits: {normal}")
