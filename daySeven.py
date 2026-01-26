# List
# A list is a collection of multiple values stored in a single variable
# List is mutable (Changable)

mylist = [10,12,13,10,"bird",5.5,[13,[13,10],10],[13,10],True]

# In list indexing starts from 0 (+ve indexing) left to right
# list indexing starts from -1 (-ve indexing) Right to left

data = [10,"hello",3.5,True]

# print(data[2])
# print(data[3])

#Mutable
data[3]="Tejaswini"
# print(data)

# lenght len()
# print(len(data))

# ["sumer","kunali","sarthak","dishant"  "saniya" , "vaibhav",]

# Append(value)
# new value add karta hai
# value add sabse last me add hongi
data.append(50)
print(data)

# Insert(index,value)
data.insert(1,"Namaste")
print(data)

# Remove()
data.remove("hello")
print(data)

# Pop()
data.pop(2)
print(data)

# Sort()

numeric=[55,10,12,13,14,90]
# numeric.sort()
# print(numeric)

# Reverse()
# numeric.reverse()
# print(numeric)

# print(numeric[0])

# Slicing [startswith:Endswith]
print(numeric[0:4]) # 4 excluded

































