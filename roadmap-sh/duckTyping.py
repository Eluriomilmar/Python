class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

class Car:

    alive = False

    def speak(self):
        print("Honk!")


Animals = [Dog(), Cat(), Car()]

for animal in Animals:
    animal.speak()
    print(animal.alive)