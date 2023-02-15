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

#Read:

def read():
    if os.path.exists(file):
        with open(file, "r") as f:
            print(f.read())
    else:
        print("𝙁𝙞𝙡𝙚 𝙙𝙤𝙚𝙨𝙣'𝙩 𝙀𝙭𝙞𝙨𝙩")

def rename():
    new_file = input("𝐄𝐧𝐭𝐞𝐫 𝐅𝐢𝐥𝐞 𝐍𝐚𝐦𝐞~")
    if os.path.exists(file):
        os.rename(file, new_file)
        print("𝗧𝗵𝗲 𝗙𝗶𝗹𝗲 𝗛𝗮𝘀 𝗕𝗲𝗲𝗻 𝗥𝗲𝗻𝗮𝗺𝗲𝗱 ✔")

    else:
        print("𝙁𝙞𝙡𝙚 𝙙𝙤𝙚𝙨𝙣'𝙩 𝙀𝙭𝙞𝙨𝙩")
