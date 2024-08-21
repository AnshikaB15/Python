"""
    Print Multiplication Table of the first 20 numbers.

    Output should be -

                Multiplication Table for 1
                ==========================
                1 X 1 = 1
                1 X 2 = 2
                ....
                1 X 10 = 10

                ....
                .....
                
                Multiplication Table for 20
                ===========================
                20 X 1 = 20
                20 X 2 = 40
                ....
                20 X 10 = 200
"""

for no in range(1, 21):
    print()
    print("Multiplication Table for {}".format(no))
    print("===========================")
    for time in range(1, 11):
        print("{} X {} = {}".format(no, time, no * time))


