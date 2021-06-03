# Python Program to enter any alphabet and test alphabet is ‘a’ or not
# BASIC Format
"""

Cls
Input “Enter the alphabet”;A$
A$=UCase$ (A$)
Select Case A$
Case ‘A’
Print “It’s alphabet A”
Case Else
Print “It’s not alphabet A” 
End Select 
End 

"""

# Python Format
from functions import clrscr

clrscr()
letter = input("Enter any Alphabet(A-Z): ")
print("It’s alphabet A") if letter.lower() == 'a' else print("It’s not alphabet A")