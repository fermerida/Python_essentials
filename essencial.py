import os
from order import *
from punctuation import *


clear = lambda: os.system('cls') #on Windows System
clear()
print("This is a python essential string modifications")
string = input("Enter a string:\n")

while True:
    clear()
    print("The String is: "+string)
    print("Select a string modification")
    print("1. Order words alphabetically")
    print("2. Remove punctuation")
    print("3. Pass to Uppercase")
    print("4. Pass to Lowercase")
    print("5. Exit")

    sel = input()
    print("You selected "+str(sel))
    if sel == "1":
        order(string).do()
    elif sel =="2":
        punct(string).do()
    elif sel =="3":
        print(string.upper())
    elif sel =="4":
        print(string.lower())
    elif sel == "5":
        break
    input("Press enter")
    


