# Exception Handling
# Exception Handling is way to handle runtime error so that the program should not crash and run contineously

# Problem without exceptional Handling

# while True :
#     num = int(input("Enter your number\n"))
#     print(10/num)

# syntax 
# try and except

# try :
#         # risky code
# except:
#     # error handle

# while True :
#     try : 
#         num = int(input("Enter your number\n"))
#         print(10/num) 
#     except:
#         print("Warning !! kuch to error aaya hai fix karde")


# try :
#     # risky code
# except:
#     # error handle
# else :
#     # sirf tab chalega jab error na aaye
# finally :
#     # Hamesha chalega


# while True :
#     try : 
#         num = int(input("Enter your number\n"))
#         result=10/num 
#     except:
#         print("Warning !! kuch to error aaya hai fix karde")
#     else : 
#         print("Division Succesfull")
#         print("Result is",result)
#     finally:
#         print("Program finished")


# # Practice Code

balance =1000
while True:
    try :
        amount = int(input("Enter amount to withdraw\n"))

        if amount <= 0 :
            raise ValueError("Amount should be greter than 0 and positive hona chahiye")
        
        if amount > balance:
            raise Exception("Insufficient Balance")
        
        balance -= amount

    except ValueError as s:
        print("Invalid input",s)

    except Exception as e:# while True :
        print("Transaction Failed",e)

    else :
        print("Withdraw Successfull")
        print("Your Remaining Balance is",balance)
    finally:
        print("Thank you for banking with ICICI")


# Exception --> base class

# ValueError
# TypeError
# KeyError
# IndexError
# ZeroDivisionError









