word_list = ["ardvark", "babboon", "camel"]

#TODO1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase

#TODO3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
# import random
#
# chosen_word = random.choice(word_list)
#
# guess = input("Guess a letter: ").lower()
#
# for letter in chosen_word:
#     if letter == guess:
#         print("Right")
#     else:
#         print("wrong")

#step 2
import random
word_list = ["ardverk", "baboon", "camel"]
chosen_word = random.choice(word_list)

print(f"Pssst, the solution is {chosen_word}")
#TOD01: Create an empty list called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_"] with 5 "_" representing each letter to guess.

guess = input("Guess a letter: ").lower()




