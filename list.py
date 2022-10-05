fruits = ['apple', 'peach', 'melon', 'grapes']

hetro_list = ['string', 1, 3.4, True, fruits]


# print(hetro_list)
# print(fruits[0])
# print(fruits[-1])
# print(hetro_list[-1][-1])

# 26. list method

# append
print(fruits)
fruits.append('banana')
print(fruits)

# insert
print(fruits)
fruits.insert(3, 'lemon')
print(fruits)

# delete
fruits.remove('peach')
print(fruits)

# sort 1
fruits.sort()
print(fruits)

# sort2
fruits.sort(reverse=True)
print(fruits)

# len 
print(len(fruits))