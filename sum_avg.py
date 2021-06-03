# Python Program to enter any three numbers,sum and the average
# BASIC Format
"""

Cls
Input " Enter any number" ;A
Input " Enter any number" ;B
Input " Enter any number" ;C
Let Sum = A+B+C
Let Average =Sum/3
Print" The sum=" ;Sum
Print" The Average is " ;Average
End

"""

# Python Format
from functions import clrscr

clrscr()
a = int(input("Enter no 1: "))
b = int(input("Enter no 2: "))
c = int(input("Enter no 3: "))
total = a + b + c
avg = total / 3
print(f"The sum of {a},{b} & {c} = {total}\nThe average of {a},{b} & {c} = {avg}")