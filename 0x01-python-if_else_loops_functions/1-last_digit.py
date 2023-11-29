#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    digit = number % 10
else :
    digit = -((-number) % 10)
print('Last digit of {} is {} {}'.format(number, digit, "and is greater than 5" if digit > 5 else "and is 0" if digit == 0 else "and is less than 6 and not 0" if digit < 6 and digit != 0 else "ok"))
