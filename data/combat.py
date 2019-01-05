import character
import time
from termcolor import colored



p = character.Player()

e = character.Monster()

def fight(p, e):
    next_hit_p = 0
    next_hit_e = 0
    hit = 100


    while True:

        def hitting(att, _def):
            dmg = att.str - _def.armor
            dmg_col = colored(str(dmg), 'red', attrs=['bold'])
            print(f"{att.name} did {dmg_col} damage to {_def.name}")
            _def.health -= dmg
            health_col = colored(str(_def.health), 'red', attrs=['bold'])
            print(f"{_def.name} has {_def.health} health remaining.")
            print(" ")


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


        time.sleep(0.1)

    print(f"{winner.name} wins!")
    print(f"{winner.name} has {winner.health} health left.")
    return winner

def encounter(p, e):
    winner = fight(p, e)
    if winner == p:
        p.gain_exp(10)
        p.gold += e.gold
        
