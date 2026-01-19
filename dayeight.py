# Dictionary
# -------------

# A dictionary where we store the data in keys & values pairs
# words ---> meaning 
{"name":"Sumer"}

# KeyPoint
# -------------
# Data stored in key : Values
# key must be unique
# values can be anything
# Dict is mutable(changable)
# written in  {}

mydict ={
        "name":"Manju",
        "age":20,
        "city":"Wardha",
        "college":"FEAT"
        }

# Print dict
# -------------
print(mydict)

# Access Value
# -------------
# print(mydict["name"])
# print(mydict["age"])

# Change Value
# -------------
# mydict["name"] = "Ranju"
# mydict["college"]="Tulsiram"
# print(mydict)

# Add new key and Value
# -------------
# mydict["Department"]="B.tech"
# print(mydict)

# Remove Data
# -------------
# mydict.pop("age")
# print(mydict)

# Check key exist 
# -------------

# if "name" in mydict:
#     print("Yes name is present in the dict",mydict["name"])
# else:
#     print("Name not exist")

# print(mydict["name"])

# Get() example
# -------------
# print(mydict.get("name"))

# keys() get all keys
# -------------
# print(mydict.keys())
 
# values() get all values
# -------------
# print(mydict.values())

# items() get all key -value pair
# -------------
print(mydict.items())
# print(mydict)

# pop() remove item
# -------------
print(mydict.pop("name"))
# print(mydict)

# popitem() remove last item
# -------------
# mydict.popitem()
# print(mydict)

# clear()
# -------------
# mydict.clear()
# print(mydict)

# copy()
# -------------
dicttwo=mydict.copy()
print(dicttwo)

# update()
# -------------
# mydict["city"]="Chandrapur"
# mydict.update({"city":"chandrapur",'college': 'Agnihotri'})
# print(mydict)

# setdefault() agar hai to rakho nahi hai to add krdo
# -------------
# student={}
# student.setdefault("name","rahul")
# print(student)









