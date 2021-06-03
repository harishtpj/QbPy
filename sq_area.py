# Python Program to find the area of the square
# BASIC Format
"""

Cls
Input" Enter the number" ;n
Let square= n^2
Print" The area of square=" ;Square
End

"""

# Python Format
from functions import clrscr

clrscr()
square = int(input("Enter the number: "))
area_square = square ** 2
print(f"The area of square = {area_square}")