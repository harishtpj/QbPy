# Python Program to find 10%,20% and 30% of the input number
# BASIC Format
"""

Cls
Input" Enter any number" ;N
Let T=10/100*N
Let Twe=20/100*N
Let Thi=30/100*N 
Print " 10%of input number=" ;T
Print " 20%of input number=" ;Twe
Print " 30%of input number=" ;Thi 
End

"""

# Python Format
from functions import clrscr

clrscr()
num = float(input("Enter any number: "))
p10 = (10/100) * num
p20 = (20/100) * num
p30 = (30/100) * num
print(f"10% of {num} = {p10}")
print(f"20% of {num} = {p20}")
print(f"30% of {num} = {p30}")