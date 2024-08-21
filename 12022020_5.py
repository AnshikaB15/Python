# This program handles the Exception thrown by is_odd() function, by using 'except' block

import MyModule

try:
    if(MyModule.is_odd(10)):
        print("Given number is Odd")
    else:
        print("Given number is Even")
    
    if(MyModule.is_odd("abcd")):
        print("Given number is Odd")
    else:
        print("Given number is Even")

except Exception as e:
    print(e)
