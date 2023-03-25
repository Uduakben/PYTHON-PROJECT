#Instruction: use the best data structure to determine the number of occurence of a letter then print out the letter exceptionally
sentence = "How many letters appear in this sentence"
from pprint import pprint
letters = {}
for letter in sentence:
    if letter in letters:
        letters[letter] += 1
    else:
        letters[letter] = 1
pprint(letters, width=10)

