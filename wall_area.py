# Python Program to find the area of four walls of a room
# BASIC Format
"""

Cls
Input"Enter the height ";H
Input"Enter the length "; L
Input"Enter the Breadth";B
Let A= 2 * H * (L+B)
Print " The area of four walls =";A
End

"""

# Python Format
from functions import clrscr

clrscr()
height = int(input("Enter the Height: "))
length = int(input("Enter the Length: "))
breadth = int(input("Enter the Breadth: "))
area = 2 * height * (length + breadth)
print(f"The area of four walls = {area}")