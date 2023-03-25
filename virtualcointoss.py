import random


print("Welcome to the Virtual Coin Toss Program")
random_side = random.randint(0, 1)
if random_side == 1:
    print("Heads")
else:
    print("Tails")
print(random_side)