import random
#rules of Rock Paper Scissors

#rule 1: rock wins against scissors
#rule 2: scissors wins against paper
#rule 3: paper wins against rock

user_choice  = int(input("What are you choosing: 0 for rock, 1 for paper, 2 for scissors? \n"))
computer_choice = int(random.randint(0,2))
print(f"computer choose {computer_choice}")

if user_choice == 0 and computer_choice == 2:
    print("You win")
elif computer_choice > user_choice:
    print("You loose")
elif user_choice == computer_choice:
    print("its a draw, try again!")
elif computer_choice == 0 and user_choice == 2:
    print("You loose")
elif user_choice > computer_choice:
    print("You win")
else:
    print("Sorry you just typed an invalid number")