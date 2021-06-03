# Python Program to convert the distance from miles to kilomiles
# BASIC Format
"""

Cls
Input " Enter the length in miles";M
Let K=M*1.6
Print" The length in kilo miles=";K
End

"""

# Python Format
from functions import clrscr

clrscr()
miles = int(input("Enter the length in miles: "))
km = round(miles*1.609,3)
print(f"The Length in Kilo meter = {km}")