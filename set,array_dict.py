#set
#We use a curly bracket {} to define a set
#it is a collection of no duplicate of data in a sequence be it unordered or ordered
# set_of_number = {1,2,1,3,5,5,6,4}
# first = set(set_of_number)
# second = {1, 2, 7}
# second.add(8)
# second.remove(8)
# print(second)
#Get the union of two set
# print(first | second)
# #Get the intersection of two set
# print(first & second)
# #Get the difference of two set
# print(first - second)


#array
# from array import array
# numbers = array("i", [1,2,3])
# print(type(numbers))


#dictionary
#A collection of key values pairs
#we use the curly bracket to define a dictionary
# numbers2 = {"x":1, "y":2}
# numbers = dict(x=1, y=2)
# numbers["w"] = 3
# print(numbers)
# for key, values in numbers.items():
#     print(key, values)

#dictionary comprehension
# value = []
# for x in range(10):
#     value.append(x * 2)
# print(value)
# value = {x: x * 2 for x in range(10)}
# print(value)
#
# #A simple task to round it up
# from pprint import pprint
# sentence = "How many letters appear in this sentence and the numbers of times"
# letters = {}
# for letter in sentence:
#     if letter in letters:
#         letters[letter] += 1
#     else:
#         letters[letter] = 1
# pprint(letters, width=10)
# values = []
# for items in range(10):
#     values.append(items * 4)
# print(values)
# values = [x * 4 for x in range(10)]
# print(values)
