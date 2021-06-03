# Python Program to check the numbers between 1 & 3
# BASIC Format
"""

Cls
Input “Enter the numbers between 1-3”;N
Select case N
Case 1
Print “It’s number 1”;
Case 2
Print “It’s a number 2”;
Case 3
Print “It’s a number 3”
Case else 
Print “It’s out of range”;
End select
End 

"""

# Python Format
from functions import clrscr

clrscr()
num = int(input("Enter the numbers between 1-3: "))
if num == 1:
    print("It’s number 1")
elif num == 2:
    print("It’s number 2")
elif num == 3:
    print("It’s number 3")
else:
    print("It’s out of range")