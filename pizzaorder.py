print("Welcome to Python Pizza Deliveries!")
size = input("What size of pizza do you want? S, M, or L\n").upper()
with_hotdog = input("Do you want hotdog? Y or N \n").upper()
extra_chicken = input("Do you want extra chicken? Y or N\n").upper()

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if with_hotdog == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
if extra_chicken == "Y":
    bill += 1

print(f"Your final bill is ${bill}")
