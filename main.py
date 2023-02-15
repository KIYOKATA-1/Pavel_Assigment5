import os

#Create File:

file = "file.txt"

#Create Menu with Options:

menu = {
  "1": "Create File",
  "2": "Add Data",
  "3": "Read",
  "4": "Rename File",
  "5": "Delete",
  "6": "Exit"
}

#Function for get user input:

def menu():
    print("\n•••••••MENU•••••••")
    for option in menu:
        print(f"{option}. {menu[option]}")
    return input("Ｃｈｏｓｅ Ｏｐｔｉｏｎ")

