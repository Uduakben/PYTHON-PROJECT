#[] this is used to define a list or a sequence of object
#list of numbers or integers
# chars = ["a", "b", "c"]
# numbers = [1,2,3]
# join = chars + numbers
# print(join)
# zeros = [0] * 20
# print(zeros)
# new_numbers = list(range(10))
# print(new_numbers)
# string = list("Welcome")
# print(len(string))

#ACCESSING ITEMS IN A LIST
# letters = ["a", "b", "c", "d"]
# print(letters[0])
# numbers = list(range(20))
# print(numbers[::2])
# print(numbers[::-1])

#LIST UNPACKING
# numbers = [1,2,3,4, 5,6,7,7,8,9]
# first,  *others, last, = numbers
# print(first, last)

#first = numbers[0]
# second = numbers [1]
# third = numbers [2]
# print(third)

#LOOPING OVER A LIST
# letters = ["a", "b", "c"]
# for letter in letters:
#     print(letter)
#get index position of each letter
# letters = ["a", "b", "c"]
# for letter in letters:
#     print(letter)

#ADDING AND REMOVING ITEMS FROM A LIST
#When a function is part of an object we call the function a method

#ADd
# letters = ["a", "b", "c",]
# letters.append("d")
# print(letters)
#
# #Add at a particular position
# letters.insert(0,"-")
# print(letters)
#
# #Removing items from a list
# letters.pop()
# print(letters)
#
# #want to remove a letter and don't know the index
# letters.remove("b")
# print(letters)
#
# #remove range of numbers
# del letters[0:3]
# print(letters)
#
# #clear all object in a list
# letters_new = ["a","b", "c","d","e"]
# letters_new.clear()
# print(letters_new)

#finding items in a list
letters = ["a", "b", "c"]
#how to get the index position of letter "a" in the list
# print(letters.index("a"))
# if "d" in letters:
#     print(letters.index("d"))
#using the count method
# print(letters.count("c"))

#SORTING LIST
# numbers = [3,51,2,8,6]
# numbers.sort()
#how to sort in descending order
# numbers.sort(reverse=True)
# print(numbers)
# print(sorted(numbers))
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]
# def sort_item(item):
#     return item[1]
#
#
# items.sort(key=sort_item)
# print(items)
#USING THE LAMBDA


# items.sort(key=lambda item:item[1])
# print(items)
# prices = []
# for item in items:
#     prices.append(item[1])

prices = list(map(lambda item:item[1], items))
prices.sort()
print(prices)

# prices = list(map(lambda item:item[1], items))

# print(prices)

#FILTER FUNCTION
# filtered = list(filter(lambda item: item[1] >= 10, items))
# print(filtered)
#list comprehension
#mapping
# prices = [item[1] for item in items]
# print(prices)
#filtering
# filtered = [item for item in items if item[1] >= 10]
#ZIP
# list1 = [1,2,3]
# list2 = [10, 20, 30]
# print(list(zip(list1,list2)))

#STACK
# browsing_session = []
# browsing_session.append(1)
# browsing_session.append(2)
# browsing_session.append(3)
# print(browsing_session)
# last = browsing_session.pop()
# print(last)
# print(browsing_session)
# print("redirect", browsing_session)
# if not browsing_session:
#     print(browsing_session[-1])

# from collections import deque
# queue = deque([])
# queue.append(1)
# queue.append(2)
# queue.append(3)
# queue.popleft()
# print(queue)
# if not queue:
#     print("empty")

#TUPLE(THIS IS A READ ONLY LIST)
# point = tuple([1,2])
# print(point)