# If-else statement
# if else is a decision making statement in python that allows the program to choose 
# one block of code out of two or more options based on conditions

# Syntax
# ------

# if condition:
#     # code run when condition true
# else:
#     # code run when condition is false

# ==================================

# age = int(input("Enter your age"))

# if age >= 18:
#     print('You are eligible for voting')
# else:
#     print('You are minor')

# elif

# mark = int(input("Enter your mark"))

# if mark >= 90:
#     print("You are excellent")
# elif mark >=60:
#     print("You are best")
# else:
#     print("You are avg")


# year = int(input("Enter year"))

# if year == 2025:
#     print("This is current year")
# elif year < 2025:
#     print("This is previous year")
# else:
#     print("This is future year")

# check if the day is weekend or not 

# day = input("Enter day").lower()

# if day =="saturday" or day == "sunday":
#     print("this is weekend day")
# else:
#     print("this is week day")


age = int(input("Enter your age"))

if age >= 18 and age <= 22:
    print("Eligible for driving licence")
else:
    print("Not eligible")









