#  Python Program to find out the simple Interest and the Amount
# BASIC Format
"""

Cls
Input " Enter the Principal";P
Input " Enter the Rate";R
Input " Enter the Time";T
Let I = P*T*R/100
Let A= P + I 
Print " The simple Interest = ";I
Print " The amount=";A
End

"""

# Python Format
from functions import clrscr

clrscr()
p = int(input("Enter the Principal: "))
r = float(input("Enter the Rate: "))
t = int(input("Enter the Time: "))
si = round(((p*r*t)/100),2)
amt = p + si
print(f"The simple Interest = {si}\nThe amount = {amt}")