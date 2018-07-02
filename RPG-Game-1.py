#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

class Hero:
    def __init__(self, health, power)
        self.health = 10
        self.power = 5
    def attack(self, goblin):
        goblin.health -= self.power
        if goblin.health <= 0
            print("the goblin is dead")
    def print_status(self):
        print("You have {} health and {} power.".format(hero_health, hero_power))


class Goblin:      
    def __init__(self, health, power)
        self.health = 6
        self.power = 2
    def attack(self, hero):
        hero.health -= self.power
        if hero.health <= 0:
            print("You are dead")
    def print_status(self):
        print("The goblin has {} health and {} power.".format(goblin_health, goblin_power))

# melissa = Hero(10,2)
# veronica = Goblin(6,3)

# melissa.attack(veronica)

def main():
    while goblin.alive() and hero.alive():
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            # Hero attacks goblin
            hero.attack(goblin)
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if goblin_health > 0:
            # Goblin attacks hero
            goblin.attack(hero)
                print("You are dead.")

main()