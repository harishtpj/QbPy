# Python program to return Square and Cube of number
# BASIC Format
"""

Cls
Input" Enter the number" ;n
Let square= n^2
Let Cube = n^3 
Print" The area of square=" ;Square
Print" The area of cube=" ; Cube
End

"""

# Python Format
from functions import clrscr

clrscr()
number = int(input("Enter a number: "))
square = number ** 2
cube = number ** 3
print(f"The square of {number} = {square}\nThe cube of {number} = {cube}")