# Python program to enter name, city, country, age and print them
# BASIC Format
"""

CLS
Input " Enter the name ";N$
Input " Enter the city";C$
Input " Enter the country";CO$
Input " Enter the age";A
Print " The name is ";N$
Print " The city is ";C$
Print " The country is ";CO$
Print " The age is ";A
End 

"""

# Python format
from functions import clrscr

clrscr()
name = input("Enter the name: ")
city = input("Enter the city: ")
country = input("Enter the country: ")
age =  int(input("Enter the age: "))
print(f"""\n\nThe name is {name}.
The city is {city}.
The country is {country}
The age is {age}""")
