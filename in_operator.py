# in operator
fruits = ['apple', 'peach', 'melon', 'grapes']
# print('apple' in fruits)

# print('h' not in 'hello')

# challenge 1
user_input = input("What kind of furits do you like?")

if user_input in fruits:
    fruits.remove(user_input)
else:
    fruits.append(user_input)

print("Here are the fruits we have {}".format(fruits))