class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is asleep.")


class Predator(Animal):
    def hunt(self):
        print("This animal is hunting")

class Prey(Animal):
    def flee(self):
        print("This animal is fleeing")

class Dog(Predator, Prey):
    race = "dog"
    def speak(self):
        print("woof!")


class Cat(Predator):
    race = "cat"
    def speak(self):
        print("meow!")


class Mouse(Prey):
    race = "mouse"
    def speak(self):
        print("squeak")
