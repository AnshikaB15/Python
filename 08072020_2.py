
"""
    Finding age in years, months, days.


        2020-08-07

        2019-19-37
        2008-10-13
        ==========
          11-09-24
        ==========

"""

import datetime as dt

today = dt.date.today()
print("Today is {}".format(today))

birthDays = int(input("Enter your day of birth (1..31): "))
birthMonth = int(input("Enter your month of birth (1..12): "))
birthYear = int(input("Enter your year of birth (2000, 2001 etc): "))

resultDays = today.day
resultMonth = today.month
resultYear = today.year

# We will borrow 30 days if needed, and reduce one month
if resultDays < birthDays:
    resultDays = resultDays + 30
    resultMonth = resultMonth - 1

# We will borrow 12 months if needed, and reduce one year
if resultMonth < birthMonth:
    resultMonth = resultMonth + 12
    resultYear = resultYear - 1

resultDays = resultDays - birthDays
resultMonth = resultMonth - birthMonth
resultYear = resultYear - birthYear

print("Your age is {} years, {} months, and, {} days".format(resultYear, resultMonth, resultDays))







