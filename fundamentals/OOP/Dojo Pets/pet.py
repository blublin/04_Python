import random

class Pet:
    def __init__(self, name , petType , tricks, health, energy):
        self.name = name
        self.petType = petType
        self.tricks = tricks
        self.health = health
        self.energy = energy

    # sleep() - increases the pets energy by 25
    def sleep(self):
        self.energy += 25
        print(f"{self.name} slept!")
        print(f"{self.name}'s energy levels rose to {self.energy}")
        return self
    # eat() - increases the pet's energy by 5 & health by 10
    def eat(self, food):
        self.energy += 5
        self.health += 10
        return self
    # play() - increases the pet's health by 5
    def play(self):
        self.health += 5
        return self
    # noise() - prints out the pet's sound
    def noise(self):
        print(f"{self.name} let out a loud, joyfull bark!")
        return self
    def do_trick(self):
        print(f"{self.name} did an awesome {self.tricks[random.randint(0,(len(self.tricks)-1))]}")
        return self


class anotherPetClass(Pet):
    def __init__(self, name , petType , tricks, health, energy, somethingExtra):
        super().__init__(name , petType , tricks, health, energy)
        self.thatSuperSomethingExtra = somethingExtra