# Python program to find the area of the triangle
# BASIC Format
"""

Cls
Input " enter the base" ;b
Input " enter the height" ;h 
let T = 1/2*b*h
Print" The area of triangle=" ;T
End

"""

# Python Format
from functions import clrscr

clrscr()
base = int(input("Enter the Base: "))
height = int(input("Enter the Height: "))
area = (1/2) * base * height
print(f"The area of triangle = {area}")