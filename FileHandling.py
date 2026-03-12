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

# file = open("example.txt","r")
# name= file.read()
# print(name)
# file.close()

# Write File (write file karne se jo purana data rahega vo gayab hojayega)
# file = open("example.txt","w")
# file.write("My name is Manju")
# file.close()

#append
# file = open("example.txt","a")
# file.write("\nMy name is Sarthak")
# file.close()


# In industry generally we use "with" instead of close()
# - Automatic close hojata
# - ye safe mode hai


# with open("example.txt","a") as doc:
#     doc.write("\nMy name is Aman")




# ================================================

# Stored Name

# studentName = input("Enter Student Name")

# with open("example.txt","a") as db:
#     db.write(f"\n{studentName}")


# Read all data

# with open("example.txt","r") as db:
#     content = db.read()
#     print(content)

# Read single line

# with open("example.txt","r") as db:
#     content = db.readline()
#     print(content)

# Read multiple lines

# with open("example.txt","r") as db:
#     content = db.readlines()
#     print(content[1])


# create file 

# with open("tejaswini.txt","x") as db:
#     db.write("Hi myself ranju this is my first file")
#     print("Filed created and data added")


with open("photo-1485470733090-0aae1788d5af.jpg","rb") as db:
    content=db.read()
    print(content)


with open("Hello.jpg","wb") as db:
    db.write(content)

     
    

