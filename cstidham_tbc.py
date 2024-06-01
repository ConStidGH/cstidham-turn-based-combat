# Connor Stidham
# TBC module
# 5-31
# TBC module defining class character and their functions

import random

class Character:
    def __init__(self, name="Character", health=10, hit=50, maxDamage=5, armor=2):
        self.name = name
        self.health = health
        self.hit = hit
        self.maxDamage = maxDamage
        self.armor = armor

    def stats(self):
        print(f"Name: {self.name}")
        print(f"Health: {self.health}")
        print(f"Hit Chance: {self.hit}%")
        print(f"Max Damage: {self.maxDamage}")
        print(f"Armor: {self.armor}")

    def alive(self):
        return self.health > 0

    def plyrDamage(self, damage):
        armorAbsorb = max(0, damage - self.armor)
        self.health -= armorAbsorb
        print(f"{self.name} is hit for {armorAbsorb} damage. Hit Points left: {self.health}")

    def attack(self, target):
        if random.randint(1, 100) <= self.hit:
            damage = random.randint(1, self.maxDamage)
            print(f"{self.name} hits {target.name} for {damage} damage!")
            print("")
            target.plyrDamage(damage)
        else:
            print(f"{self.name} misses the attack on {target.name}!")
            print("")

def fight(hero, monster):
    turn = 1
    while hero.alive() and monster.alive():
        print(f"Turn {turn}")
        hero.attack(monster)
        if monster.alive():
            monster.attack(hero)
        
        turn += 1

        if hero.alive() and monster.alive():
            input("Press Enter to continue to the next turn.")
            print("")
        
        hero.attack(monster)
        if monster.alive():
            monster.attack(hero)
    
    if hero.alive():
        print(f"{hero.name} wins the fight!")
    else:
        print(f"{monster.name} wins the fight!")