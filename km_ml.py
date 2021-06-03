# Python Program to convert the distance from kilometer to miles
# BASIC Format
"""

Cls
Input"Enter the length in kilometer";K
Let M= K / 1.6

Print "The length in miles =";M
End

"""

# Python Format
from functions import clrscr

clrscr()
km = int(input("Enter the length in kilometer: "))
miles = round(km / 1.609,3)
print(f"The length in miles = {miles}")