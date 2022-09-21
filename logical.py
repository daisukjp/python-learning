# logical operators
# and, or , not
from tkinter.messagebox import YES


a = 1
b = 1
c = 10
d = 100
print(a == b and c > d)
# false
print(a == b or c > d)
# true
print(not a == b)
# false

# challenge1
age = 13
height = 1400

print(age >= 10 and height >= 110)

# challenge2
master = False
job_experience = 6
print(master or job_experience >= 5)