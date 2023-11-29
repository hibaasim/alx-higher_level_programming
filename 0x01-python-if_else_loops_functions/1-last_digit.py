#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
status = "and is greater than 5"
stat2 = "and is less than 6 and not 0"
if number >= 0:
    digit = number % 10
else:
    digit = -((-number) % 10)
if digit > 5:
    print('Last digit of {} is {} {}'.format(number, digit, status))
elif digit == 0:
    print('Last digit of {} is {} {}'.format(number, digit, "and is 0"))
elif digit < 6 and digit != 0:
    print('Last digit of {} is {} {}'.format(number, digit, stat2))
