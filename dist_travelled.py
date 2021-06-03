# Python Program to enter the initial mileage(m1) and final mileage (m2) then calculate the distance traveled
# BASIC Format
"""

CLS
Input "Enter the Initial Mileage";M1
Input "Enter the Final Mileage";M2
Let D= M2-M1
Print " The distance covered=";D
End

"""

# Python Format
from functions import clrscr

clrscr()
m1 = int(input("Enter the Initial Mileage: "))
m2 = int(input("Enter the Final Mileage: "))
distance = m2 - m1
print(f"The distance covered = {distance}")