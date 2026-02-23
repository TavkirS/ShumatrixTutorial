# File Handling
# File handling is the process of creating , reading , writing , and
# managing the files using a programming language

# syntax

# file = open("yaha aap file ka path donge","mode[kis nature me aapko open karna hai]")

# Files Modes

# Mode   Meaning
# "r" --> read
# "w" --> write
# "a" --> append
# "x" --> create new file
# "rb" --> read binary
# "wb" --> write binary

# Steps
# 1) File Open Karo
# 2) Read/Write karo
# 3) Close

# Read file

# file = open("file.txt","r")
# name= file.read()
# print(name)
# file.close()

# Write File (write file karne se jo purana data rahega vo gayab hojayega)
# file = open("file.txt","w")
# file.write("Ham aajse File Handling sikh rahe hai")
# file.close()

#append
# file = open("file.txt","a")
# file.write("\nHam Ranju Manju and shruti Sarthak available hai")
# file.close()


# In industry generally we use "with" instead of close()
# - Automatic close hojata
# - ye safe mode hai


# with open("file.txt","r") as sumer:
#     content = sumer.read()
#     print(content)



# ================================================

# Stored Name
# studentName = input("Enter Student Name")

# with open("file.txt","a") as db:
#     db.write(f"\n{studentName}")


# Read all data

# with open("file.txt","r") as db:
#     content = db.read()
#     print(content)

# Read single line

# with open("file.txt","r") as db:
#     content = db.readline()
#     print(content)

# Read multiple lines

# with open("file.txt","r") as db:
#     content = db.readlines()
#     print(content)


# create file 

# with open("Shrutifile.txt","x") as db:
#     db.write("Hi myself shruti this is my first file")
#     print("Filed created and data added")


with open("Screenshot 2026-02-09 224836.png","rb") as db:
    content=db.read()
    print(content)


with open("sir.png","wb") as db:
    db.write(content)

     
    

