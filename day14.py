# Function
# Jisse bar bar use kr sakte
# Function is a block of code that does one specific job and can be used again and again

# Syntax of Function
# def (define) is a keyword in python 

# def function_name():
    # business logic


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
# hellow("Tejaswini")

# name--> parameter 
# "sarthak"--> argument (value)




name = "sumer"

# print(name.upper()) function without param in python
# print(len(name)) function with param in python

# hellow("Shruti")
# hellow("Sarthak")
# hellow("Manju")
# hellow("Kunali")
# hellow("Ranju")

# lets make calcu

# def add(a,b):
#     print(a + b)

# add(15545,54545)



# Function with return value

# def square(a):
#     total = a*a
#     return total

# value=square(95)
# print(value)

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
    
# print(check_even(21))

# result = check_even(81)
# print(result)

# Function calling anathor function

# def add(a,b):
#     return a+b

# def show():
#     print(add(2,8))

# show()

# name = "Shruti"

# print(len(name))


# =========Exercise==================

# def snapchatWellcome():
#     print("Hello welcome to the snapchat","Manju")

# # snapchatWellcome()

def snapchatWellcome(name,age):
    print(f"Hello {name} welcome to the snapchat your age is {age}")


# snapchatWellcome("kunali",20)
# snapchatWellcome("Shruti",65)

# ========================

# def checkOddEven(num):
#     if num % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"
    
# print(checkOddEven(2))

# ========================


def countString(message):
    totallen = message.count("i")
    return totallen

print(countString("Tejaswini"))



# ===========================


# def calculator(num1,sign,num2):
#     if sign == "+":
#         print(num1+num2)
#     elif sign == "-":
#         print(num1-num2)
#     elif sign == "*" or sign == "x":
#         print(num1*num2)
#     elif sign == "/":
#         print(num1/num2)    
 
# calculator(8,"+",9)






