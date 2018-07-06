import random
#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

class Character:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power
    
    def alive(self):
        if self.health > 0:
            return True
        if self.name == "Zombie":
            return True
    
    def attack(self, enemy):
        enemy.health -= self.power
        self.health -= self.power

        
        if self.name == "Hero":
            print("You do {} damage to the goblin.".format(self.power))
            r = random.randint(1,10)
            print("check random number:{}".format(r))
            if r <= 2:
                enemy.health -= self.power

        if enemy.name == "Medic":
            r = random.randint(1, 10)
            if r <= 2:
                enemy.health += 2
                print("{} gained 2 health-points.".format(enemy.name))

        if enemy.name == "Shadow":
            r = random.randint(1, 10)
            if r <= 1:
                enemy.health -= self.power
            else:
                print("{} wasnt damaged!".format(enemy.name))

        if enemy.name == "Wizard":
            r = random.randint(1, 10)
            if r <= 5:
                ememy.health += 5
                print("The {} gained 5 health-points".format(enemy.name))

        if enemy.name == "Bat":
            r = random.randint(1,10)
            if r <= 3:
                enemy.health +=2
                self.health -+ 2
                print("The {} took 2 health-points fromt the {}.".format(enemy.name, self.name))

        if not enemy.alive():
            print("The goblin is dead")

            shopping.goShop(self)

        elif enemy.name == "Hero":
            print("The {} does {} damage to you.".format(self.name, self.power))
            if not enemy.alive():
                print("You are dead.")

        if enemy.health <= 0 and enemy.name != "Zombie":
            print("{} is dead.".format(enemy.name))
            self.coins += enemy.bounty
            print("{} gains {} bounty by defeating {}.".format(self.name, enemy.bounty, enemy.name)) 

        elif enemy.health <= 0 and enemy.name == "Zombie":
            print("The {} never dies.".format(enemy.name))      

        # shopping.goShop(self)

    def print_status(self):
        #print("You have {} health and {} power.".format(self.health, self.power))
        print("The {} have {} health, and {} power.".format(self.name, self.health, self.power))

class Hero(Character):
    def __init__(self, name, power, health):
        super().__init__(name, power, health)
        self.coins = 10

    def buy(self, item):
        self.coins -= item.cost
        print("Your coin balance is {}.".format(self.coins))
        print(item)
        item.apply(self)

class Goblin(Character):
    def __init__(self, name, power, health):
        super().__init__(name, power, health)
        self.bounty = 5

class Medic(Character):
    def __init__(self, name, power, health):
        super().__init__(name, power, health)
        self.bounty = 3

class Shadow(Character):
    def __init__(self, name, power, health):
        super().__init__(name, power, health)
        self.bounty = 5

class Zombie(Character):
    def __init__(self, name, power, health):
        super().__init__(name, power, health)

class Wizard(Character):
    def __init__(self, name, power, health):
        super().__init__(name, power, health)
        self.bounty = 6

class Bat(Character):
    def __init__(self, name, power, health):
        super().__init__(name, power, health)
        self.bounty = 8

class superTonic:
    cost = 5
    name = "Super tonic"
    def apply(self, character):
        character.health = 10
        print("{} health is now {}".format(character.name, character.health))

class Armour:
    cost = 10
    name = "Armour"
    def apply(self, character):
        character.armour += 2
        print("{} armour was increased to {}.".format(character.name, character.armour))

class Evade:
    cost = 5
    name = "Evade"
    def apply(self, character):
        character.evade += 2
        print("{} evade amount increased to {}.".format(character.name, character.evade))

class MagicPowder():
    cost = 10
    name = "Magic Powder"
    def apply(self, character):
        character.power += 10
        print("The magic powder increased {}'s power.".format(self.power))

class Knife:
    cost = 15
    name = "Knife"
    def apply(self, character):
        character.power += 15
        print("The knife increased {}'s power by {}".format(character.name, character.power))

class Shop():
    items = [superTonic(), Armour(), Evade(), MagicPowder(), Knife()]
    def goShop(self, hero):
        while True:
            print("You have {} coins.".format(hero.coins))
            print("What do you want to do?")
            for i in range(0, len(Shop.items)):
                item = Shop.items[i]
                print("{} get {} for {} coins".format(i + 1, item.name, item.cost))
            print("6 to leave")
            ans = int(input("> "))
            if ans == 6:
                break
            else:
                toBuy = Shop.items[ans - 1]
                print(toBuy)
                hero.buy(toBuy)

hero = Hero("Hero", 20, 5)
enemy = Goblin("Goblin", 15, 2)
medic = Medic("Medic", 3, 5)
shadow = Shadow("Shadow", 1, 3)
zombie = Zombie("Zombie", 10, 5)
wizard = Wizard("Wizard", 5, 4)
bat = Bat("Bat", 8, 5)
shopping = Shop()
tonic = superTonic()
armour = Armour()
evade = Evade()
powder = MagicPowder
knife = Knife()
# fight(hero, goblin)

def main():
    
    while enemy.alive() and hero.alive():
        hero.print_status()
        enemy.print_status()
        print()
        print("What do you want to do?")
        print("1. fight {}".format(enemy.name))
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        inp = input()
        if inp == "1":
            # Hero attacks goblin
            hero.attack(enemy)
        elif inp == "2":
            pass
        elif inp == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(inp))

        if enemy.alive():
            # Goblin attacks hero
            enemy.attack(hero)
            hero.print_status()
            enemy.print_status()
        if not enemy.alive():
            print("The goblin is dead")

        if enemy.health > 0 or enemy.name == "Zombie":
            enemy.attack(hero)

main()