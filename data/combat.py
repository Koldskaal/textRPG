
import time
from .loot_tables import grab_loot,low_level
from termcolor import colored
from random import choice,randint

import sys
if sys.stdin.isatty():
    import colorama
    colorama.init(convert=True)




def fight(p, e):
    next_hit_p = 0
    next_hit_e = 0
    hit = 10


    while True:

        def hitting(att, _def):
            dmg = att.str + choice([randint(0,int(att.str*0.1)),-randint(0,int(att.str*0.1))]) - _def.armor
            dmg_col = colored(str(dmg), 'red', attrs=['bold'])
            print(f"{att.name} attacks!")

            _def.health -= dmg
            health_col = colored(str(_def.health), 'green', attrs=['bold'])
            print(f"{_def.name} took {dmg_col} damage (HP left: {health_col})")
            # print(f"{_def.name} has  health remaining.")
            print("-"*15)


        next_hit_p += p.agi
        next_hit_e += e.agi

        if next_hit_p > hit:
            hitting(p, e)
            next_hit_p -= hit
            if e.health <= 0:
                winner = p
                break

        if next_hit_e > hit:
            hitting(e, p)
            next_hit_e -= hit
            if p.health <= 0:
                winner = e
                break


        time.sleep(0.3)

    print(f"{winner.name} wins!")
    print(f"{winner.name} has {winner.health} health left.")
    return winner

def encounter(p, e):
    winner = fight(p, e)
    if winner == p:
        p.gain_exp(e.exp)
        p.gold += e.gold
        gained_items = grab_loot.grab_loot_low_level(low_level.list_of_weapons, low_level.list_of_helmets, low_level.list_of_armour, low_level.list_of_rest, 2, 5)
        print(f'You picked up: {gained_items}!')
        p.items += gained_items
        return "enemy_killed"
    else:
        print("You lose gtfo")
        sys.exit()

if __name__ == '__main__':
    import character
    p = character.Player()
    e = character.Monster()
    e.health = 100
    e2 = character.Monster()
    e2.health = 120
    e3 = character.Monster()
    e3.health = 150
    encounter(p,e)# for testing
    print(p.levelcap)
    encounter(p,e2)
    print(p.levelcap)
    encounter(p,e3)
    print(p.levelcap)
