# Python Program to enter any alphabet and find out whether it is vowel or alphabet
# BASIC Format
"""

Cls
Input “Enter Letters/Alphabet”;A$
A$ = UCase $ (A$)
Select case A$
Case “A”, “E”, “I”, “O”, “U”
Print “Its’ a vowel”
Case Else 
Print “ It’s not a vowel”
End Select
End

"""

# Python Format
from functions import clrscr

clrscr()
alpha = input("Enter Letter: ")
vowel = ['a','e','i','o','u']
print(f"{alpha[0]} is a vowel") if alpha[0] in vowel else print(f"{alpha[0]} is not a vowel")