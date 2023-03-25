#EXCEPTION
# numbers = [1, 2, 3, 4]
# #print(numbers[5])

# age = int(input("Age: "))
# print(age)

#HANDLING EXCEPTION
# try:
#     numbers = [1, 2, 3, 4]
#     print(numbers[5])
#
# except IndexError:
#     print("incorrect index position try again")
# try:
#     age = int(input("Age: "))
# except ValueError:
#     print("Please enter a valid number")
# else:
#     print("The program still continue")
# print("Please debug if faced with issues")



#HANDLING DIFFERENT EXCEPTION
# try:
#     age = int(input("Age: "))
#     division = 20 / age
#
# except (ValueError, ZeroDivisionError):
#     print("invalid input and pls input must not be zero")
#
# else:
#     print("Program Continues")

#cleaning up of external resources
# try:
#     file = open("exceptions.py")
#     print("file opened")
#     age = int(input("Age: "))
#     division = 20 / age
#
#
# except (ValueError, ZeroDivisionError):
#      print("invalid input and pls input must not be zero")
#
# else:
#      print("Program Continues")
# finally:
#     file.close()

#the with statement
# try:
#     with open("exceptions.py") as file:
#         print("file opened")
#     print("file opened")
#     age = int(input("Age: "))
#     division = 20 / age
#
# except (ValueError, ZeroDivisionError):
#      print("invalid input and pls input must not be zero")
#
# else:
#      print("Program Continues")

#raising exception and cost of raising exception in python
#python 3 built in exceptions
from timeit import timeit

code1 = """
def calc_division(age):
    if age <= 0:
        raise ValueError("The Age must not be less than or equal to zero")
    return 20 / age
try:
    calc_division(-5)
except ValueError as error_message:
    print(error_message)
    
"""

print(timeit(code1, number=10000))