# What is python
# Python is a high-level, easy-to-learn, powerful programming language used 
# for web development, automation, data science, AI, and more.
# ===============================

# Print Statement
print("Helloo Tejaswini")
# ===============================

#  Variables
# -----------
# Variables are use to store data
# Python has no command for declaring a variable.
# A variable is created the moment you first assign a value to it.
# Pythons predefined keywords should not be variable name (35 predefined "hard" keywords)
# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 
# 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

num = "Sarthak"

# ===============================

# Naming Rules for Python variables
# -------------------------
# myname
# my_name
# myNameIs => camel case
# MyNameIs => pascal case
# my_name_one  => snake case

# ===============================

# Many Values to Multiple Variables
# ---------------------------------
# name1, name2, name3 = "Kunali", "Sarthak" , "Taukir"

# name1 = "Kunali"
# name2 = "Sarthak"
# name3 = "Taukir"
# print(name1)
# name1, name2, name3 = "Sarthak", "Rajesh" , "Taukir"
# name1 = name2 = name3 = "Sarthak"
# print(name2)

# ===============================

# One Value to Multiple Variables
# ---------------------------------
x = y = z = "Orange"
print(y,x,z)

# ===============================
# print()
# In the print() function, you output multiple variables, separated by a comma:
# You can also use the + operator to output multiple variables:
# (+ , ",")

name = "Sarthak"
age = "is"
roll = "Engg"

name="Priy"
dob="1998"
print(name+dob)
# print(name,age,roll)
# print(name+age+roll)

# ===============================

# Global Variable
# ---------------
# Variables that are created outside of a function (as in all of the examples above) are known as global variables.
# Global variables can be used by everwhere throughout the page, both inside of functions and outside.
# A variable that is declare inside the function is called local variable
x= "Sarthak is awsome"

def myfun():
    global xy
    xy="Tejawini is brillent"
    print(xy)

myfun()
print(xy)
# print(x) 

# ===============================

