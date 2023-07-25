#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
last_digit = number % 10
print("Last digit of {} is {} ".format(number, last_digit))
if last_digit > 5:
    print1 = print("and is greater than 5")
elif last_digit == 0 :
    print2 = print ("and is 0")
elif last_digit < 6 and last_digit != 0: 
    print3 = print ("and is less than 6 and not 0")
else: print(last_digit)