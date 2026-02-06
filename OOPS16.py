# class Mobile():
#     #Class attributes
#     brand = "Samsung"
#     price = 15000

#     def show_details(self):
#         print("Brand:", Mobile.brand)
#         print("Price:", Mobile.price)

#     def update_price(self, new_price):
#         Mobile.price = new_price
#         return Mobile.price

# Oppo = Mobile()
# Oppo.show_details()
# price=Oppo.update_price(18000)
# print(price)


# class Student():

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def show_details(self):
#         print("Name:", self.name)
#         print("Age:", self.age)

#     def is_adult(self):
#         if self.age >= 18:
#             print("Student is an adult")
#         else: 
#             print("Student is not an adult")

# s1 = Student("Rahul", 20)
# s1.show_details()
# s1.is_adult()

# class Bank():

#     account_Type = "Saving Account"
#     balance = 1000

#     def show_balance(self):
#         print("Bank:", Bank.account_Type)
#         print("Balance:", Bank.balance)

#     def deposit(self, amount):
#         Bank.balance = Bank.balance + amount

#     def withdraw(self, amount):
#         if amount <= Bank.balance:
#             Bank.balance = Bank.balance - amount
#         else:
#             print("Insufficient balance")


# acc1 = Bank()

# acc1.show_balance()
# acc1.deposit(500)
# acc1.show_balance()
# acc1.withdraw(2000)
# # acc1.show_balance()



# class Library():
#     library_name = "City Library"
#     total_books = 100

#     def show_details(self):
#         print("Library Name:", Library.library_name)
#         print("Total Books:", Library.total_books)

#     def add_books(self, count):
#         Library.total_books = Library.total_books + count

#     def remove_books(self, count):
#         if count <= Library.total_books:
#             Library.total_books = Library.total_books - count
#         else:
#             print("Not enough books available")

# l1 = Library()
# l1.show_details()
# l1.add_books(20)
# l1.show_details()
# l1.remove_books(50)
# l1.show_details()




# class Car():
#     company = "Tata"
#     fuel = "Petrol"

#     def details(self):
#         print("Company:", Car.company)
#         print("Fuel Type:", Car.fuel)

#     def change_fuel(self, new_fuel):
#         Car.fuel = new_fuel

# c1 = Car()
# c1.details()
# c1.change_fuel("Diesal")
# c1.details()




# class Employee:

#     company_name = "Infosys"
#     salary = 25000

#     def show_info(self):
#         print("Company:", Employee.company_name)
#         print("Salary:", Employee.salary)

#     def increment(self, amount):
#         Employee.salary = Employee.salary + amount

# e1 = Employee()
# e1.show_info()
# e1.increment(1500)
# e1.show_info()


# class OnlineCourse():
#     course_name = "Python Basics"
#     duration_days = 30
#     fees = 5000

#     def show_course(self):
#         print("Course Name:", OnlineCourse.course_name)
#         print("Duration (Days):", OnlineCourse.duration_days)
#         print("Fees:", OnlineCourse.fees)

#     def change_fees(self, new_fees):
#         OnlineCourse.fees = new_fees

#     def extend_duration(self, extra_days):
#         OnlineCourse.duration_days = OnlineCourse.duration_days + extra_days

# c1 = OnlineCourse()
# c1.change_fees()
# c1.change_fees("taukir@gmail.com")
# c1.extend_duration(30)
# c1.show_course()