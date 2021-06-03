# Python Program to input student's name,marks obtained in four different subjects,find the total and average marks
# BASIC Format
"""

Cls
Input" Enter the name " ;N$
Input" Enter the marks in English" ;E
Input" Enter the marks in Maths" ;M
Input" Enter the marks in Science" ;S
Input" Enter the marks in Nepali" ;N 
Let S=E+M+S+N
Let A=S/4
Print " The name of the student is" ;N$
Print " The total marks is" ;S
Print " The Average marks" ;A
End 

"""

# Python Format
from functions import clrscr

clrscr()
name = input("Enter your name: ")
english = float(input("Enter the marks in English: "))
maths = float(input("Enter the marks in Maths: "))
science = float(input("Enter the marks in Science: "))
nepali = float(input("Enter the marks in Nepali: "))
total = english + maths + science + nepali
avg = total / 4
print(f"The name of the student is {name}")
print(f"\t- Total Marks = {total}")
print(f"\t- Average Marks = {avg}")