# String
# String is a collection of charaters  

# we can give string number(123), Symbol(!@%#&!*), letter(abcs)
# we can write the the string in either ex. "" or ''
# Immutable string change nhi hoti  (Unchangeable)
# left indexing start from 0 
# right indexing starts from -1

name="    aman    "
name2="TAUKIR"
msg="Wellcome to 9 th @string chapter"

# String Operations
# ====================

# len()
# lenofname = len(name2)
# print(lenofname)

# Indexing
# print(name2[1])
# print(name2[-1])

# Slicing [startswith:endswith] endswith excluded
# print(name2[0:3])

# Upper()
# print(name.upper())

# Lower()
# print(name2.lower())

# strip() remove extra spaces
# print(name)
# print(name.strip())

# replace() old text ko new text se replace kardega
# print(msg.replace("9","10"))
# print(msg.replace("Wellcome","Namaste"))

# find() subtring ka index batata hai
text ="very veryyyy memmorable day"
# print("*******")
# print(text.find("y"))

# count() kitne baar ek word letter aaya hai
# print(text.count("day"))

# spilt() string ko list me tod dega

# greeting ="very very memmorable day"
# print(greeting.split())

# join() list ko string me jod denga
# greeting2 =['very', 'very', 'memmorable', 'day']
# print(" ".join(greeting2))


# isalpha() check karta hai string me sirf alphabet hain ya nahi 

check = "Rahul"
# print(check.isalpha())

# isdigit() check karta hai sirf number hai ya nahi

number="15454"
# print(number.isdigit())

# isalnum() check karta hai alphabet + number (no special charater) rahna chahiye
alnum = "123asd"
# print(alnum.isalnum())

# isspace() space hai ya nhi

space2 ="" # ye sirf empteness check karta hai 
# print(space2.isspace())

# capitalize() first letter capital karega
name3 ="sumer"
# print(name3.capitalize())

# title() har words ka first letter capital karega

text="my name is sarthak"
# print(text.title())

# swapcase() Capital <---> small switch karta hai

myname= "taukir"
# print(myname.swapcase())

myname2= "TAVKIR"
# print(myname2.swapcase())

myname3= "TAvKiR"
# print(myname3.swapcase())

# center() text ko beach me align karega

# print(myname.center(100,"*"))

# format() string value me insert karega (Most Imp)

name4 = "Sarthak"
age = 21
gao="Deoli"
print("Happy Birthday Taukir and your age is 24")
# print("Happy birthday {} and your age is {} ".format(name4,age))

# F-string (IMPORTANT)
# below method use in industry to handle the string format this is modern aur fast way to format the string
print(f"Happy birthday {name4} and your age is {age} you are from {gao}")


# escape charater \n ,\t

print("Hello\nWorld") # new line me shift honga
print("Hello\tWorld") # ek tab ki space create hongi

# String Comparison

print("apple"=="apple")

# string Concatenation string ko jodna

a="Hello"
b="World"
print(a+" "+b)

# string repetation string ko repeat karta hai

print("Kunali"*3)

# startwith() check karta hai ki string kisi specific word/letter se start ho raha ya nahi 
# endswith() check karta hai ki string kisi specific word/letter se khatam/end ho raha ya nahi 

language ="Python Program"
# print(language.startswith("Program"))
print(language.endswith("Program"))


# ===================*****************====================




























































