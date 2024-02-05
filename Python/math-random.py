#Math and random modules

# https://docs.python.org/3/library/math.html

import math

num = int(input("Give me a number to find the square root for: "))
print(math.sqrt(num))

print('---------------------------------------')

# https://docs.python.org/3/library/random.html

import random
print("Printing random number")
print(random.random())

print('--------------------------------------')

import random
print("Printing random integer", random.randint(0, 1000))
print("Printing random integer", random.randrange(0, 10))
