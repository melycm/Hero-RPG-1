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
    
    def attack(self, enemy):
        enemy.health -= self.power
        self.health -= self.power
        if self.name == "Hero":
            print("You do {} damage to the goblin.".format(self.power))
        if not enemy.alive():
            print("The goblin is dead")
        elif enemy.name == "Hero":
            print("The {} does {} damage to you.".format(self.name, self.power))
            if not enemy.alive():
                print("You are dead.")

    def print_status(self):
        #print("You have {} health and {} power.".format(self.health, self.power))
        print("The {} have {} health and {} power.".format(self.name, self.health, self.power))

class Hero(Character):
    def __init__(self, name, power, health):
        super().__init__(name, power, health)

class Goblin(Character):
    def __init__(self, name, power, health):
        super().__init__(name, power, health)

def main():
    hero = Hero("Hero", 10, 5)
    enemy = Goblin("Goblin", 6, 2)
    # fight(hero, goblin)

    
    while enemy.alive() and hero.alive():
        hero.print_status()
        enemy.print_status()
        print()
        print("What do you want to do?")
        print("1. fight goblin")
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
    # 

main()