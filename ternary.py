print("Welcome to the University Summit Program")

name = input("Kindly enter your name: \n")
age = int(input("Kindly enter your age: \n"))

# if age >= 18:
#     print("Eligible")
# else:
#     print("Not Eligible")
message = "Eligible" if age >= 18 else "Not Eligible"
print(message)