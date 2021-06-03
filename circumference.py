# Python Program to find the circumference of the circle
# BASIC Format
"""

Cls
Input" Enter the radius " ;R
Let Circumference=22/7*R*2
Print " The area of circle =" ;Circumference
End 

"""

# Python format
from functions import clrscr
import math

clrscr()
radius = int(input("Enter the radius: "))
circumference = round(2 * math.pi * radius,2)
print(f"The Circumference of circle = {circumference}")