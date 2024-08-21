import math

# Some functions present in Python's built-in 'math' module
# List of all 'math' module functions @ https://www.w3schools.com/python/module_math.asp
print(math.sqrt(64))
print(math.pi)
print(math.ceil(4.56))
print(math.floor(4.56))
print(math.trunc(4.56))

import calendar as cal
# print(cal.calendar(2020))

import datetime as dt
print(dt.date.today())
print(dt.datetime.now())

today = dt.date.today()
print("Today is {}, the {} of Month# {} in the Year# {}".format(today.strftime("%A"), today.day, today.strftime("%B"), today.year))


