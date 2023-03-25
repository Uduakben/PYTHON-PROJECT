import random


#rules of rockpaper scissors
#Rock wins against scissors
#Scissors win against paper
#Paper wins against rock
user_choice = input("What do you choose? Type 0 for Rock, 1 for paper or 2 for scissors.")
computer_choice = random.randint(0,2)
print(f"Computer choose {computer_choice}")

if user_choice == 0 and computer_choice == 2:
    print("You win!")
if computer_choice > user_choice:
    print("You loose")
elif computer_choice == user_choice:
    print("its a draw")
elif computer_choice == 0 and user_choice == 2:
    print("You loose")
elif user_choice > computer_choice:
    print("You win!")
# elif user_choice >= 3 or user_choice < 0:
#     print("invalid number you loose")
else:
    print("You type an invalid number you loose!")