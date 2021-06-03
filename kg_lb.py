# Python Program to convert the weight from kilogram to pounds
# BASIC Format
"""

CLS
Input"Enter the weight in kilogram";K
Let P=K*2.2
Print "The pound is ";P
End

"""

# Python Format
from functions import clrscr

clrscr()
kg = int(input("Enter the weight in kilogram: "))
lb = kg * 2.2
print(f"The pound is {lb}")