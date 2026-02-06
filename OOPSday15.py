# Object Oriented Programming (OOPS) is a programming approach are
# buit using object that represent real world entites, 
# and these objects contain data(attributes) and behaviour(methods)

# every object has:
# Data (attributes/properties/variable)
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
# Living room

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

# s1= Student()
# print(s1.name)
# print(s1.age)

# Explanationss:
# s1--> object
# Student() --> is class ka object banao
# . --> Object ke data ko access karna / adreess or referance Point

# note: class name should be start with CAPITAL 
# Letter and the name should be meaningfull


# An object is an instance of a class,it represents a real world entity 
# and can access the data and methods defined in a class


class Car():
    color1="Green"
    color2="Red"
    withac=True
    withoutac=False

# Har object apna alag identity rakhta hai
# object bolete class ka real use 

# bmw = Car()
# print(bmw.color2)
# print(bmw.withac)

# audi = Car()
# print(audi.color2,audi.withac)

# Class Methods
# A method is a function that is defined inside a class and is
# used to perform an action on object.
# Self current object ko refer karta hai 

# class Car():
#     color ="Red" # this is variable/attribute
#     wheels = 4  # this is variable/attribute

#     def carDrive(self,name):
#         self.name1=name
#         print("Car Start",self.name1)

#     def acOn(self):
#         print("AC on")

#     def soundON(self):
#         print("Music ON")

# bmw = Car()
# bmw.carDrive("Kunali")
# bmw.acOn()


# Constructer
# ------------

# __init__() this is a special method that is 
# automatically called when object is created


# class Game():
#     def __init__(self):
#         print("Sarthak")
#         print("Shruti")
#         print("Ranju")
#         print("Manju")
#         print("taukir")
#         print("Tejaswini")
    
#     def actionUp(self):
#         print("this method jump the object")

#     def actionDown(self):
#         print("this method down the object")

# freefire = Game()
# freefire.actionUp()
# freefire.actionDown()


# Inheritance
# Inheritance allows a class (child) to reuse properties and methods of anathor class i.e (parent)
# Inheritance means parent class ki cheezien child class me use karna

class Vehicle():
    color1="Red"
    color2="Black"
    fourwheel=4
    twowheel=2

    def Start(self):
        print("Gaddi Start")
    
    def Stop(self):
        print("Gaddi Stop")

class Car(Vehicle):

    def Acstart(self):
        print("Car AC start")

class Bike(Car):

    def Onstand(self):
        print("Bike on Stand")


bmw = Bike()
bmw.Start()
bmw.Acstart()
bmw.Onstand()
# bmw
# 
# 
# 
# 
# .Onstand()


# Polymorphism
# Polymorphism means the ability of a method or function to take multiple forms same name but different behavior
# Polymorphism like ek hi naam but different alag alag kaam

# Method Overiding(Most Common)

# class Animal():
#     def sound(self):
#         print("Animal makes sound")


# class dog():
#     def sound(self):
#         print("Dog Barking")
    
# a = Animal()
# d = dog()

# a.sound()
# d.sound()



class Shape():

    color ="red"
    color1 = "Green"

    def __init__(self):
        print("I am a shape predictor")

    def circle(self):
        print("I am a circle")

    def rectangle(self):
        print("I am a rectangle")
    
obj = Shape()
obj.circle()
obj.rectangle()

class Shape1(Shape):

    def hexagon(self):
        print("This is hexagon")

obj = Shape1()
obj.circle()
obj.hexagon()



class Animal():

    animalColor = "White"
    AnimalColor2 ="Black"

    def walk(self):
        print("animal walking")

    def animalSound(self):
        print("Animal sounding")


tiger = Animal()
print(tiger.animalColor)
tiger.walk()




































  



















