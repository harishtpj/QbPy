# Python Program to find the volume of the box
# BASIC Format
"""

Cls
Input " enter the length " ;l
Input " enter the breadth " ;b 
Input " enter the height " ;h
Let Volume= l*b*h
Print" The volume of box =" ;Volume
End 

"""

# Python Format
from functions import clrscr

clrscr()
length = int(input("Enter the Length: "))
breadth = int(input("Enter the Breadth: "))
height = int(input("Enter the Height: "))
volume = length * breadth * height
print(f"The volume of box = {volume}")