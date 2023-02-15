import os

#Create File/Файл жасау:

file = "file.txt"

#Create Menu with Options/Параметрлері бар мәзір жасау:

option_menu = {
  "1": "Create File",
  "2": "Add Data",
  "3": "Read",
  "4": "Rename File",
  "5": "Delete",
  "6": "Exit"
}

#Function for get user input/Пайдаланушы енгізуін алуға арналған функция:

def menu():
    print("\n•••••••MENU•••••••")
    for option in menu:
        print(f"{option}. {menu[option]}")
    return input("Ｃｈｏｓｅ Ｏｐｔｉｏｎ")

#Create/Жасау
def create_file():
    if os.path.exists(file):
        print("••🅵🅸🅻🅴 🅸🆂 🅰🅻🆁🅴🅰🅳🆈 🅴🆇🅸🆂🆃•••")
    else:
        with open(file, "w") as f:
            print("ꜰɪʟᴇ ʜᴀꜱ ʙᴇᴇɴ ᴄʀᴇᴀᴛᴇᴅ ✔")

#Add Data/Деректерді қосу:

def add():
    if os.path.exists(file):
        data = input("𝙀𝙣𝙩𝙚𝙧 𝘿𝙖𝙩𝙖 𝙏𝙤 𝘼𝙙𝙙: ")
        with open(file, "a") as f:
            f.write(data + "\n")
            print("𝘿𝙖𝙩𝙖 𝙝𝙖𝙨 𝙗𝙚𝙚𝙣 𝙖𝙙𝙙𝙚𝙙 𝙩𝙤 𝙩𝙝𝙚 𝙛𝙞𝙡𝙚")
    else:
        print("𝙁𝙞𝙡𝙚 𝙙𝙤𝙚𝙨𝙣'𝙩 𝙀𝙭𝙞𝙨𝙩")

#Read/Оку:

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

#Delete/Жою:

def delete():
    if os.path.exists(file):
        os.rename(file)
        print("𝐅𝐈𝐋𝐄 𝐇𝐀𝐒 𝐁𝐄𝐄𝐍 𝐃𝐄𝐋𝐄𝐓𝐄𝐃")
    else:
        print("𝙁𝙞𝙡𝙚 𝙙𝙤𝙚𝙨𝙣'𝙩 𝙀𝙭𝙞𝙨𝙩")

#Define Main Function/Негізгі функцияны анықтаңыз:

def main():
    while True:
        option = menu()
        if option == "1":
            create_file()
        elif option == "2":
            add()
        elif option == "3":
            read()
        elif option == "4":
            rename()
        elif option == "5":
            delete()
        elif option == "6":
            break
        else:
            print("𝐈𝐧𝐯𝐚𝐥𝐢𝐝 𝐒𝐲𝐧𝐭𝐚𝐱!!!")
