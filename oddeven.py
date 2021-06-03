# Python Program to enter any number and find out whether it is even or odd
# BASIC Format
"""

Cls
Input “Enter any number” ;N
R=N mod 2
Select case R
Case = 0 
Print “The number is Even number”
Case Else
Print “The number is odd number”
End Select
End

"""

# Python Format
from functions import clrscr

clrscr()
num = int(input("Enter any number: "))
print(f"{num} is Even number") if num % 2 == 0 else print(f"{num} is odd number")