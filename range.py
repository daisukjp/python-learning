# range (start, stop, step)
# for i in range(1, 7, 1):
#     print(i)

# challenge fizzBuzz
for i in range(1, 51):
    if i % 15 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)