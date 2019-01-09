import time
from termcolor import colored
from random import choice,randint
import sys

try:
    from  .loot_tables import grab_loot,low_level
    from .game_log import log
except ModuleNotFoundError:
    from  loot_tables import grab_loot,low_level

text_log = ""

def add_to_text_log(text, canvas):
    global text_log
    text_log += text + "\n"
    settings = {
    'column_priority'  : 1,     # Order of who goes first from left to right
    'delay'             : 0,     # if it needs to be x lines below
    'width'             : 40,    # how wide will it add_to_text_log
    'allignment'        : '<',
    'max_lines'         : 20,    # for the string that keeps getting bigger. Take only the latest 30
    'join_char'         : '',
    'title'             : 'LOG'
    }
    canvas.add_to_print('log', text_log, settings)
    canvas.print_canvas()


def fight(p, e):
    next_hit_p = 0
    next_hit_e = 0
    hit = 50

    while True:

        def hitting(att, _def):
            a_name = att.name if att.name != p.name else 'you'
            d_name = _def.name if _def.name != p.name else 'you'

            dmg = att.str + choice([randint(0,int(att.str*0.1)),-randint(0,int(att.str*0.1))]) - _def.armor
            dmg_col = colored(str(dmg), 'red', attrs=['bold'])
            log.add_to_log(f"{a_name.capitalize()} {'attack' if a_name == 'you' else 'attacks'}!", 'Combat')

            _def.health -= dmg
            health_col = colored(str(_def.health), 'green', attrs=['bold'])
            max_health = colored(str(_def.max_health), 'green', attrs=['bold'])
            log.add_to_log(f"{d_name.capitalize()} took {dmg} damage.", 'Combat', 'bad' if _def.name == p.name else 'default')
            if _def.health <= 0:
                log.add_to_log(f"WOAH! {d_name.capitalize()} has no more health left!", 'Announcer', 'surprise')
            # log.add_to_log("-"*40, 'Combat')


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

        log.print_canvas()
        time.sleep(0.2)

    log.add_to_log(f"{winner.name} wins!", 'Announcer', 'surprise')
    return winner

def encounter(p, e):
    log.print_canvas(clear=True)
    winner = fight(p, e)
    if winner == p:
        p.gain_exp(e.exp)
        p.gold += e.gold
        gained_items = grab_loot.grab_loot_low_level(low_level.list_of_weapons, low_level.list_of_helmets, low_level.list_of_armour, low_level.list_of_rest, 2, 5)
        log.add_to_log(f'You picked up: {gained_items}!', 'Info', 'useful')
        p.items += gained_items

        return "enemy_killed"
    else:
        log.add_to_log("You lose gtfo", 'Announcer', 'surprise')
        sys.exit()

if __name__ == '__main__':
    import character
    if sys.stdin.isatty():
        import colorama
        colorama.init(convert=True)
    p = character.Player()
    e = character.Monster()
    e.health = 100
    e2 = character.Monster()
    e2.health = 120
    e3 = character.Monster()
    e3.health = 150
    encounter(p,e)# for testing
    log.add_to_log(p.levelcap)
    encounter(p,e2)
    log.add_to_log(p.levelcap)
    encounter(p,e3)
    log.add_to_log(p.levelcap)
