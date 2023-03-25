#ACCESSING ITEMS IN A LIST
# letters = ["x", "y", "p", "z"]
# print(letters[0])
# numbers = [1,2,3,4,5,6,7,8,9,10,11]
# print(numbers[::-1])
# numbers =list(range(15))
# print(numbers[0:15])

#LIST UNPACKING
# numbers = [7, 9,6,10,8,29,11,2,6,0,4]
# first,second,third, *others = numbers
# first = numbers[0]
# second = numbers [1]
# third = numbers [2]
# fourth = numbers[3]
# print(*others)

#HOW TO ADD AND REMOVE ITEMS FROM A LIST
letters = ["x", "y", "p", "b", "w"]
# letters.append("h")
# print(letters)
# letters.insert(3, "j")
# print(letters)
# letters.pop(2)
# print(letters)
# letters.remove("b")
# print(letters)
# del letters[0:3]
# print(letters)

#FINDING ITEMS ON A LIST
# letters = ["a","b","c","d", "b", "e","a", "a"]
# print(letters.count("b"))


# SORTING LIST
# number = [1,6,8,4,90,78]
# # number.sort()
# print(sorted(number))
#
# goods = [
#     ("unit1", 15),
#     ("unit2", 13),
#     ("unit3", 18)
# ]
#
# def sorted_goods(good):
#     return good[1]
#
#
#
# goods.sort(key=sorted_goods)
# print(goods)
# print(number)
# # MAP
# # LAMBDA
# # ZIP

# from collections import deque
#
# queue = deque([])
# queue.append(1)
# queue.append(2)
# queue.append(3)
#
# print(queue)

# point = tuple([1, 2])
# print(point[1])

#USING ARRAYS IN PYTHON
# from array import array
#
# numbers = array("i", [1, 2, 3])
# numbers[1] = 1

#SET
#A collection with no duplicate
# numbers = [1, 1, 2, 3, 4]
# uniques = set(numbers)
# print(uniques)

#DICTIONARY
#This is a collection of key value pairs
# point = {"x":True, "y":2}
# point = dict(x=1, y=2)
# point["x"] = 10
# point["z"] = 20
# if "a" in point:
#     print(point["a"])
# print(point.get("a", 0))
# del point["x"]
# print(point)
# for key, values in point.items():
#     print(key, values)

#dictionary comprehension
# values = {}
# for x in range(5):
#     values[x] = x * 2
# print(values)
#     values.append(x * 2)

# values = {"x": x * 2 for x in range(5)}
# print(type(values))

#Generator Expression

# from sys import getsizeof
# values = (x * 2 for x in range(10000))
# print(type(getsizeof(values)))

# values = list(range(5))
#
# print(*values)
# from pprint import pprint
# sentence = "This is a common interview question"
# char_frequency = {}
# for char in sentence:
#     if char in char_frequency:
#         char_frequency[char] += 1
#     else:
#         char_frequency[char] = 1
# char_frequency_sorted = (sorted(char_frequency.items(),
#                                 key=lambda kv:kv[1],
#                                 reverse=True))
# pprint(char_frequency_sorted, width=10)












