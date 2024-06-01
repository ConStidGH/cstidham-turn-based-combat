# Connor Stidham
# TBC Execute
# 5-31
# Imports TBC module and executes game code

import cstidham_tbc

def main():
    hero = cstidham_tbc.Character()
    hero.name = "Bart"
    hero.health = 10
    hero.hit = 60
    hero.maxDamage = 7
    hero.armor = 2

    monster = cstidham_tbc.Character("Homer", 20, 30, 7, 0)

    hero.stats()
    print("")
    monster.stats()
    print("")

    cstidham_tbc.fight(hero, monster)

if __name__ == "__main__":
    main()