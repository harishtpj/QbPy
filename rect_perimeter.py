# Python Program to find the perimeter of a rectangle
# BASIC Format
"""

Cls
Input " enter the length " ;l
Input " enter the breadth " ;b 
Let P=2*(l+b)
Print" The perimeter of rectangle=" ;P
End

"""

# Python Format
from functions import clrscr

clrscr()
length = int(input("Enter the Length: "))
breadth = int(input("Enter the Breadth: "))
pm = 2 * (length + breadth)
print(f"The perimeter of rectangle = {pm}")