class Animal:
    def __init__(self):
        self.weight = 56
    def move(self):
        print("Humans move as a unique threat")

    def feed(self):
        print("Animals feeds in general")

    def language(self):
        print("Humans speak different languages")

    def color(self):
        return "blue"


class Birds(Animal):
    def fly(self):
        print("Birds fly")

    def color(self):
        return "yellow"

class Dolphin(Birds, Animal):
    def swim(self):
        print("Dolphin swim as their means of movement")

    def color(self):
        return "green"




a = Animal()
d = Dolphin()

print(d.color())