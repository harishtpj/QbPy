# Python Program to find the average of three different numbers
# BASIC Format
"""

Cls
Input" Enter the number " ;A
Input" Enter the number " ;B
Input" Enter the number " ;C
Let Avg= (A+B+C)/3
Print" The average=" ;Avg
End

"""

# Python Format
from functions import clrscr

clrscr()
a = int(input("Enter no 1: "))
b = int(input("Enter no 2: "))
c = int(input("Enter no 3: "))
avg = (a + b + c) / 3
print(f"Average of {a},{b} & {c} = {avg}")