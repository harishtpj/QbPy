# Python Program to enter the Nepalese currency and covert it to Indian Currency
# BASIC Format
"""

CLS
Input “Enter the Nepalese currency” ;N
Let I = N * 1.6
Print “the Indian currency=”;I
End

"""

# Python Format
from functions import clrscr

clrscr()
npr = float(input("Enter the Nepalese currency: "))
inr = round(npr * 0.62454,2)
print(f"The Indian currency = {inr}")