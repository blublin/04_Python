import pet

class Ninja:
    def __init__(coding_master, first_name , last_name , treats , pet_food, pet):
        coding_master.first_name = first_name
        coding_master.last_name = last_name
        coding_master.treats = treats
        coding_master.pet_food = pet_food
        coding_master.pet = pet

    def walk(self):
        self.pet.play()
        return self
    def feed(self):
        if len(self.pet_food) > 0:
            print(f"Feeding {self.pet.name} some tasty {self.pet_food[-1]}")
            self.pet.eat(self.pet_food.pop())
        elif len(self.treats) > 0:
            print(f"Feeding {self.pet.name} some tasty {self.treats[-1]}")
            self.pet.eat(self.treats.pop())
        else:
            print("Oh no! I ran out of all the food. How could this happen!")
        return self
    def bathe(self):
        self.pet.noise()
        return self
    def add_food(self, food):
        self.pet_food.append(food)
        return self
    def add_treat(self, treat):
        self.treats.append(treat)
        return self

barksky = pet.Pet("Barksky", "dog", ["shake", "dance", "play dead"], 50, 50) # it's absurd to 1 line this with Ninja instantiation. ABSURD  I SAY!
ben = Ninja("lublin", "ben", ["milk bone", "milk bone", "milk bone"], ["kibble", "pizza", "burger"], barksky)

ben.feed().walk().bathe()
