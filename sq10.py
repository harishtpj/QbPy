# Python Program Write a program to print numbers 1,4,9,…upto 10th term
# BASIC Format
"""

CLS 
I=1
While I < =10
Print I^2;
I = I + 1
WEND 
END 

"""

# Python Format
from functions import clrscr

clrscr()
i = 1
while i <= 10:
    print(i ** 2)
    i += 1