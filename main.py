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

#Create File
def create_file():
    if os.path.exists(file):
        print("••🅵🅸🅻🅴 🅸🆂 🅰🅻🆁🅴🅰🅳🆈 🅴🆇🅸🆂🆃•••")
    else:
        with open(file, "w") as f:
            print("ꜰɪʟᴇ ʜᴀꜱ ʙᴇᴇɴ ᴄʀᴇᴀᴛᴇᴅ ✔")

#Add Data:

def add():
    if os.path.exists(file):
        data = input("𝙀𝙣𝙩𝙚𝙧 𝘿𝙖𝙩𝙖 𝙏𝙤 𝘼𝙙𝙙: ")
        with open(file, "a") as f:
            f.write(data + "\n")
            print("𝘿𝙖𝙩𝙖 𝙝𝙖𝙨 𝙗𝙚𝙚𝙣 𝙖𝙙𝙙𝙚𝙙 𝙩𝙤 𝙩𝙝𝙚 𝙛𝙞𝙡𝙚")
    else:
        print("𝙁𝙞𝙡𝙚 𝙙𝙤𝙚𝙨𝙣'𝙩 𝙀𝙭𝙞𝙨𝙩")

