# For loop 
# for loop ka use ek kaam ko baar baar repeat karne ke liye hota hai 
# Coding Principle --> DRY = Do Not Repeat Youself

# range()
# Syntax 
# for variable in sequence:
#     statement

# iterable jisko loop me chala sakte hai

# ✅ Iterable ex:
# String
# list
# Tuple
# range
# Dict

# ❌ Non Iterable:
# int
# Float


# range() number ki sequence ko banata hai
# print(range(500,1000))

# num = 50

# Loop on message
# for i in range(51):
#     print(i,"Sumer is great")

# for loop on list
# fruits = ["Banana","Mango","Apple","Grapes"]
# for i in fruits:
#     print(i)

# for loop on String
# str = "Python"
# for i in str:
#     print(str)


# for loop with condition (if)

for i in range(1,11):
    if i % 2 == 0:
        print(i)


# loop on dict

student = {"Name":"Aman",
           "age":20,
           "city":"Delhi"
           }

# print(student["Name"])

# for i in student:
#     print(i,":",student[i])


# keys() 

for i in student.keys():
    print(i)

# values()
for i in student.values():
    print(i)

# items()

for i , j in student.items():
    print(i,"--",j)

# Exercise

# Print numbers from 1 to 30

# for i in range(1,31):
#     print(i)

# Print Hello Sarthak 8
# for i in range(1,9):
#     print("Hello sarthak")

# Print String char
# string = "Hello Kunali"

# for i in string:
#     print(i)

# Count total character in a string

# clg = "I love to go at FEAT college"
# count = 0
# # print(len(clg))

# for i in clg:
#     count += 1
# print(count)

# Print vowels from string

# word= "education"
# print(word)

# for volvel in word:
#     if volvel in "aeiou":
#         print(volvel)


def hellow_World():
    print("Hellow World")
num = "Sumer"
i=0
while i < len(num):
    print(num[i])
    i +=1 



listnum = [10,12,13,14]
i = 0
while i < len(listnum):
    print(listnum[i])
    i +=1











































