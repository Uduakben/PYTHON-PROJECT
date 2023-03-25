# for else
successful = True
for num in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed")

#nested loop
# for x in range(5):
#     for y in range(3):
#         print(f"({x}, {y})")

#iterables
#print(type(range(5)))
#we can iterate through a list
#we can iterate through a string

# number = 100
# while number > 0:
#     print(number)
#     number = number // 2

# command = ""
# while command.lower() != "quit":
#     command = input(">")
#     print("ECHO", command)

# while True:
#     command = input(">")
#     print("ECHO", command)
#     if command.lower() == "quit":
#         break
# count = 0
# for num in range(1,10):
#     if num % 2 == 0:
#         count += 1
#         print(num)
# print(f"We have {count} even numbers"),

