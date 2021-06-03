#  Python Program to find out the simple Interest
# BASIC Format
"""

Cls
Input " Enter the Principal";P
Input " Enter the Rate";R
Input " Enter the Time";T
Let I = P*T*R/100
Print " The simple Interest = ";I
End

"""

# Python Format
from functions import clrscr

clrscr()
p = int(input("Enter the Principal: "))
r = float(input("Enter the Rate: "))
t = int(input("Enter the Time: "))
si = round(((p*r*t)/100),2)
print(f"The simple Interest = {si}")