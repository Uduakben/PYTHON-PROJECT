# command = ""
# while command.lower() != "end":
#     command = input(">>>")
#     print("alert", command)

while True:
    command = input(">>>")
    print("alert", command)
    if command.lower() == "end":
        break