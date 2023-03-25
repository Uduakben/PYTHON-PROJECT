# name_string = input("Give me everybody's names, seperated by a comma.")
# #
# names = name_string.split(",")
# print(names)
# #Get the total number of items in list
# num_items = len(names)
# #Generate random numbers between 0 and the last index.
# random_choice = random.randint(0, num_items -1)
# #Person_who_will_pay = names[random_choice]
# print(person_who_will_pay + "is going to buy the meal today!"

#for loop
# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " Pie")
#     print(fruits)

# squares = [1, 4, 9, 16]
# sum = 0
# for num in squares:
#     sum += num
# print(sum)
# list = ['larry', 'curly', 'noe']
# if 'cury' in list:
#     print ('yay')
# else:
#     print('more')

#building the hangman project
import random

word_list = ['computer', 'monitor', 'keyboard']

chosen_word = random.choice(word_list)
print(f"Pssst, the solution is {chosen_word}.")

display = []
for letter in chosen_word:
    display += "_"
print(display)
end_of_game = False
while not end_of_game:
    guess = input("Guess the missing letter to complete the word").lower()

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    print(display)

    if "_" not in display:
        end_of_game = True
        print("You win")

