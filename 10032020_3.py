"""
    Print Multiplication Table of the given Table Number.
        Ex: If table number is 5 ---> output should be --->

                5 X 1 = 5
                5 X 2 = 10
                5 X 3 = 15
                ....
                5 X 9 = 45
                5 X 10 = 50
"""

no = int(input("Enter Table Number: "))

"""
    print("{} X {} = {}".format(no, 1, no * 1))
    print("{} X {} = {}".format(no, 2, no * 2))
    print("{} X {} = {}".format(no, 3, no * 3))
"""

for time in range(1, 11):
    print("{} X {} = {}".format(no, time, no * time))


