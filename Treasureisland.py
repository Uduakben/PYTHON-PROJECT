print("Welcome to Treasure Island \n Your mission is to find the missing treasure")

choice1 = input("Please choose left or right to go through the island in finding the missing treasure: \n")
if choice1 == "left":
    choice2 = input("Please choose either swim or wait to continue the game on the island: \n")
    if choice2 == "wait":
        choice3 = input("Please choose the right color for the treasure: red, blue, yellow and green: \n")
        if choice3 == "red":
            print("danger")
        elif choice3 == "blue":
            print("game over!")
        elif choice3 == "yellow":
            print("congratulations your answer is right")
        else:
            print("Game over pls try harder next time")
    else:
        print("Game over!")

else:
    print("Sorry you just fell into a hole try again some other time")
