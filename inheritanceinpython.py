class Animal:
    def __init__(self):
        self.weight = 56
    def move(self):
        print("Humans move as a unique threat")

    def feed(self):
        print("Animals feeds in general")

    def language(self):
        print("Humans speak different languages")

class Birds(Animal):
    def fly(self):
        print("Birds fly")


class Dolphin(Animal):
    def swim(self):
        print("Dolphin swim as their means of movement")



a = Animal()
