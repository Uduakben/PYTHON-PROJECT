
#sort list
# numbers = [2,5,8,1,10,3,6]
# # numbers.sort()
# print(sorted(numbers, reverse=True))
# print(numbers)

goods = [
    ("Unit1", 20),
    ("Unit3", 15),
    ("Unit2", 40),
]

# def goods_sorted(item):
#     return item[1]


# goods.sort(key=goods_sorted)
#using the lambda

# print(goods)

#map function
# price_of_goods = list(map(lambda item:item[1], goods ))

# price_of_goods.sort()
# print(price_of_goods)
# print(price_of_goods)

#lambda function
# goods.sort(key=lambda item:item[1])

#filter function

# print(filtered)

#list comprehension
# price_of_goods = list(map(lambda item:item[1], goods ))
# prices = [item[1] for item in goods]
# prices.sort()
# print(prices)
# filtered = list(filter(lambda item:item[1] >= 20, goods))
# filtered = [item for item in goods if item[1] >= 20]
# print(filtered)

#zip function
# list1 = [3, 4, 7]
# list2 = [60, 40, 10]
# print(list(zip(list1,list2, "abc")))

#stack
#LIFO BEHAVIOURS
# browsing_session = []
# browsing_session.append(1)
# browsing_session.append(2)
# browsing_session.append(3)
# print(browsing_session)
# browsing_session.pop()
# print(browsing_session)
# if not browsing_session:
#     print("not working")
# from collections import deque
#queue
#FIFO(first in and first out)
# queue = deque([])
# queue.append(1)
# queue.append(2)
# queue.append(3)
# print(queue)
# queue.popleft()
# print(queue)

#tuple
# cordinate = tuple("hello world")
# print(type(cordinate))

#set
#A collection with no duplicate
#we use curly bracket to define set
# numbers = [1, 1, 2, 3, 4]
# first = set(numbers)
# second = {1, 5}
# second.add(5)
# second.remove(5)
# len(second)
#Get the union of two set
# print(first - second)
    #= {1, 2, 3, 4, 5}
#Get the intersection of two set
#first & second = {1}
#Get the difference btw two set
#(first - second) {2, 3, 4}
#Get the symmetric difference
#first ^ second{2, 3, 4}
#we cannot access object in set using an index


#array
# from array import array
# numbers = array("i", [1, 2, 3])
# numbers[0] = 3
# numbers.pop()
# numbers.insert(0, 6)
# print(numbers)

#Dictionary
#A collection of key value pairs
#It is used to map a key to a value
#example of this is a phone book

# point = {"x": 1, "y": 2}
# point = dict(x=1, y=2)
# point['x'] = 15
# point['z'] = 20
# if "a" in point:
#     print(point['a'])
# print(point.get("a", 0))
# del point['x']
# print(point)
# # for key in point:
# #     print(key, point[key])
# for x in point.items():
#     print(x)

# values = []
# for x in range(5):
#     values.append(x * 2)
#using list comprehension
# values = [x * 2 for x in range(5)]
# print(values)

#EXCEPTION
#Exception error is a kind of error that terminate the execution of
#a program
# numbers = [1, 2]
# print(numbers[3])

# age = int(input("Age: "))

#handling Exception
#if you don't handle a exception properly your program will crash
# try:
#     age = int(input("Age: "))
# except ValueError as ex:
#     print("You didn't enter a valid age.")
#     print(type(ex))
# else:
#     print("No exceptions were thrown")
# print("Execution continues.")

#HANDLING DIFFERENT EXCEPTIONS
# try:
#     age = int(input("Age: "))
#     xfactor = 10 / age
# except (ValueError, ZeroDivisionError):
#     print("You didn't enter a valid age.")
# # except ZeroDivisionError:
# #     print("Age cannot be zero")
#
# else:
#     print("No exceptions were thrown")
# print("Execution continues.")

#cleaning up
#There are times we need to work with external resources like
#files databases, network and so on
# try:
#     file = open("simpleworkout.py")
#     age = int(input("Age: "))
#     xfactor = 10 / age
#
# except (ValueError, ZeroDivisionError):
#     print("You didn't enter a valid age.")
#
# else:
#     print("No exceptions were thrown")
# finally:
#     file.close()
# print("Execution continues.")

#THE WITH STATEMENT
# try:
#     with open("simpleworkout.py") as file:
#         print("file opened")
#     age = int(input("Age: "))
#     xfactor = 10 / age
#
# except (ValueError, ZeroDivisionError):
#     print("You didn't enter a valid age.")
#
# else:
#     print("No exceptions were thrown")

#RAISING EXCEPTIONS
def calculate_xfactor(age):
    if age <= 0:
        raise 
    return 10 / age

print(calculate_xfactor(0))



