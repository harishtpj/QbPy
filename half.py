# Python program to take any number and find it's half
# BASIC Format
"""

Cls
Input "Enter the desired number "; N
Let H = N/2
Print "The half of the number = ";H
END

"""

# Python Format
from functions import clrscr

clrscr()
num = int(input("Enter the desired number: "))
half = round(num / 2,5)
print(f"The half of the number = {half}")