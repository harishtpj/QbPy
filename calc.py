# Python Program to enter any two numbers their Sum,Product and the Difference
# BASIC Format
"""

CLS 
Input " Enter any number" ;A
Input " Enter any number" ;B
Let Sum = A+B
Let Difference= A-B
Let Product = A*B
Print" the sum =" ;Sum
Print" the Difference =" ;Difference
Print" the Product =" ; Product
End 

"""

# Python Format
from functions import clrscr

clrscr()
a = int(input("Enter no 1: "))
b = int(input("Enter no 2: "))
total = a + b
difference = a - b
product = a * b
print(f"The Sum is = {total}\nThe Difference is = {difference}\nThe Product is = {product}")