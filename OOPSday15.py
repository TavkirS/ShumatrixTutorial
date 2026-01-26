# Object Oriented Programming (OOPS) is a programming approach are
#  buit using object that represent real world entites, 
# and these objects contain data(attributes) and behaviour(methods)

# every object has:
# Data (properties/variable)
# work (Functions/methods)

# 4 Pillers of OOPS:
# 1) Encapsulation
# 2) Inheritance
# 3) Polymorphism
# 4) Abstraction

# Importance Of OOPS:
# Large Project
# Team Work 
# Code Reuse 
# Easy to maintan

# Class:
# A class is a blueprint or template used to create object. It defines the 
# properties(Variables) and behaviors(methods) that an object will have

# Class ek naksha(Map/Blueprint) hai jiske base per ham objects banate hai

# Real life example
# House(Class)
# Room
# Color
# Washroom

# Houses(objects)
# Kunali ka ghar
# Shruti ka ghar
# Sarthak Ka ghar


# Example/Syntax:
# created class here
class Student():
    name = "Kunali"
    age = 20

# Explanation:
# class --> Keyword 
# Student --> Class Name
# name,age --> attributes/variable


# Creating object from the class

s1 = Student()
print(s1.age,s1.name)
print(s1.name)

# Explanationss:
# s1--> object
# Student() --> is class ka object banaya
# . --> Object ke data ko access karna / adreess or referance Point

# note: class name should be start with CAPITAL 
# Letter and the name should be meaningfull


# An object is an instance of a class,it represents a real world entity 
# and can access the data and methods defined in a class


class Car():
    color1="Green"
    color2="Red"
    withac="Yes"
    withoutac="No"

# Har object apna alag identity rakhta hai
# object bolete class ka real use 

# bmw = Car()
# print(bmw.color2)
# print(bmw.withac)

# audi = Car()
# print(bmw.color1,bmw.withoutac)

# Class Methods
# A method is a function that is defined inside a class and is
# used to perform an action on object.
# Self current object ko refer karta hai 

# class Car():
#     color ="Red" # this is variable/attribute
#     wheels = 4  # this is variable/attribute

#     def carDrive(self,name):
#         self.age=name
#         print("Car Start",self.age)

#     def acOn(self):
#         print("AC on")

#     def soundON(self):
#         print("Music ON")

# bmw = Car()
# bmw.carDrive("Kunali")

# __int__() this is a special method that is 
# automatically called when object is created


# class Student():
#     def __init__(self):
#         print("Sarthak")
#         print("Shruti")
#         print("Ranju")
#         print("Manju")
#         print("taukir")
#         print("Tejaswini")
    
#     def studentMarks(self):
#         print("Mai ek method hu aur student ke marks batunga")

# feat =Student()


# Inheritance
# Inheritance allows a class (child) to reuse properties and methods of anathor class(parent)
# Inheritance means parent class ki cheezien child class me use karna














