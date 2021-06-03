# Python Program to find the area of the circle
# BASIC Format
"""

Cls
Input" Enter the radius " ;R
Let C=22/7*R^2
Print " The area of circle =" ;C
End

"""

# Python Format
from functions import clrscr
import math

clrscr()
radius = int(input("Enter the radius: "))
area = math.pi * radius ** 2
print(f"The area of circle is = {round(area,2)}")