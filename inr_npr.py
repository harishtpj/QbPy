# Python Program to enter the Indian currency and covert it to Nepalese Currency
# BASIC Format
"""

CLS
Input “Enter the Indian currency” ;N
Let N = I / 1.6
Print “the Nepalese currency=”;I
End

"""

# Python Format
from functions import clrscr

clrscr()
inr = float(input("Enter the Indian currency: "))
npr = round(inr * 1.60098,2)
print(f"The Nepalese currency = {npr}")