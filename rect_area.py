# Python program to find the area of rectangle
# BASIC Format
"""

Cls
Input " enter the length " ;l
Input " enter the breadth " ;b 
let A = l*b
Print" the area of rectangle=" ;a
End

"""

# Python Format
from functions import clrscr

clrscr()
length = int(input("Enter the length: "))
breadth = int(input("Enter the breadth: "))
area = length * breadth
print(f"The area of rectangle is = {area}")