# Python Functions
import os
def clrscr():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")