# Function
# Jisse bar bar use kr sakte
# Function is a block of code that does one specific job and can be used again and again

# Syntax of Function
# def (define) is a keyword in python 

# def function_name():
#     business logic


# def hellow():
#     print("Hellow World")

# hellow()

# def --> Function banane wala keyword
# hellow --> Function ka naam
# () --> empty (koi input nhi mangra)
# (name)--> Input mangra hai 
# print("Hellow World") --> Business Logic
# function kab chalega? jab function ko call karege tab vo chalega

# Function without parameter/input
# def hellow():
#     print("Hellow World")

# hellow()

# here am calling the function
# hellow()


# Function with parameter/input
# def hellow(name):
#     print("Happy birthday to you",name)

# name--> parameter 
# "sarthak"--> argument (value)

# hellow("Shruti")
# hellow("Sarthak")
# hellow("Manju")
# hellow_World("Sarthak")
# hellow("Shruti")

# lets make calcu

# def add(a,b):
#     print(a * b)

# add(51,5)


# Function with return value

# def square(a):
#     total = a*a
#     return total

# output = square(5)
# print(output)
# output=square()
# print(output)


# Function + If else

# def check_even(num):
#     if num  % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"
    
# result = check_even(21)
# print(result)

# Function calling anathor function

# def add(a,b):
#     return a+b

# def show():
#     print(add(2,8))

# show()


# =========Exercise==================

def snapchatWellcome():
    print("Holaa welcome to the snapchat","Manju")

# snapchatWellcome()

# def snapchatWellcome(name):
#     print("Holaa welcome to the snapchat",name)

# snapchatWellcome("Shruti")

# ========================

# def checkOddEven(num):
#     if num % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"
    
# print(checkOddEven(89))

# ========================

# def countString(message):
#     totallen = len(message)
#     print(totallen)

# countString("")
# ===========================


def calculator(num1,num2,sign):
    if sign == "+":
        print(num1+num2)
    elif sign == "-":
        print(num1-num2)
    elif sign == "*" or sign == "x":
        print(num1*num2)
    elif sign == "/":
        print(num1/num2)    
 
calculator(5,8,"*")



