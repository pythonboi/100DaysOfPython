# importing the Random Module from Python

import random

# Use the Range function in the For Loop from 1 to 100

for numb in range(1, 101):
    # check if number are divisible by numb and itself
    if numb % 3 == 0:
        print("Fizz")
    elif numb % 5 == 0:
        print("Buzz")
    elif numb % 3 == 0 and numb % 5 == 0:
        print("FizzBuzz")
    else:
        print(numb)

