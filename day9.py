# String
# String is a collection of charaters  

# we can give in string number(123), Symbol(!@%#&!*), letter(abcs)
# we can write the the string in either ex. "" or ''
# Immutable string change nhi hoti  (Unchangeable)
# left indexing start from 0 
# right indexing starts from -1

name="   aman   "
name2="TAUKIR"
msg="Wellcome to 9 th @string chapter"

# String Operations
# ====================

# len()
lenofname = len(name)
# print(lenofname)

# Indexing()
# print(name[1])
# print(name[-1])

# Slicing [startswith:endswith] endswith excluded
# print(msg[0:-1])

# Upper()
# print(name.upper())


# Lower()
# print(name2.lower())

# strip() remove extra spaces
# print(name)
# print(name.strip())

# replace() old text ko new text se replace kardega
# print(msg.replace("9","10"))
# print(msg.replace("Wellcome","Thanks"))

# find() subtring ka index batata hai
text ="very very memmorable day"
# print(text.find("y"))

# count() kitne baar ek wordletter aaya hai
print(text.count("very"))

# spilt() string ko list me tod dega

greeting ="very very memmorable day"
# print(greeting.split())

# join() list ko string me jod denga
greeting2 =['very', 'very', 'memmorable', 'day']
# print(" ".join(greeting2))


# isalpha() check karta hai string me sirf alphabet hain ya nahi 

check = "Rahul1221@#@!#@!"
# print(check.isalpha())

# isdigit() check karta hai sirf number hai ya nahi

number="1212fdfdsfs312315"
# print(number.isdigit())

# isalnum() check karta hai alphabet + number (no special charater) rahna chahiye
alnum = "123abc@@#!"
# print(alnum.isalnum())

# isspace() space hai ya nhi

space = " Sumer Sheikh Khan "
space2 =" " # ye sirf empteness check karta hai 
# print(space2.isspace())

# capitalize() first letter capital karega
name3 ="sumer"
# print(name3.capitalize())

# title() har words ka first letter capital karega

text="my name is sarthak"
# print(text.title())



































