import random
print("Welcome to PyPassword Generator!")

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "."]

new_letters = int(input("How many character do you want in your password:\n "))
new_numbers = int(input("How many numbers do you want in your password:\n "))
new_symbols = int(input("How many symbols do you want in your password:\n "))

password = ""
for char in range(1, new_letters +1):
    random_char = random.choice(letters)
    password = password + random_char

for num in range(1, new_numbers +1):
    random_num = random.choice(numbers)
    password = password + random_num

for sym in range(1, new_symbols +1):
    random_sym = random.choice(symbols)
    password = password + random_sym

password_list = []
for char in range(1, new_letters +1):
    random_char = random.choice(letters)
    password_list += random_char

for num in range(1, new_numbers +1):
    random_num = random.choice(numbers)
    password_list += random_num

for sym in range(1, new_symbols +1):
    random_sym = random.choice(symbols)
    password_list += random_sym

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char
print(f" You new is password will be", password)

