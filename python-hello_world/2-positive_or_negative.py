#!/usr/bin/python3
import random
number = random.randint(-10, 10)
# YOUR CODE HERE
if number > 0:
    print(number,"number is positive")
elif number == 0:
    print(number,"number is zero")
else:
    print(number,"number is negative")
