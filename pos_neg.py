# Python Program to enter any number and find out whether it is negative or positive
# BASIC Format
"""

CLS
Input “Enter the number”; N
If N>0 Then
Print “ The number is positive”
Else
Print “The number is negative”
EndIf
End 

"""

# Python Format
from functions import clrscr

clrscr()
num = float(input("Enter a number: "))
print("The number is positive") if num > 0 else print("The number is negative")